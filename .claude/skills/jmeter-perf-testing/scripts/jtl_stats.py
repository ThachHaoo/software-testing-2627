#!/usr/bin/env python3
"""Tính số liệu "sự thật" từ file .jtl (CSV có header) – dùng làm stats_truth cho bước 7 (đối chiếu phân tích AI).

Theo label + Total: count, errors, error %, mean, min, max, p50/p90/p95/p99, throughput (req/s),
KB/s nhận/gửi; timeline theo phút (count, lỗi, mean, p95, max allThreads); mã phản hồi lỗi + thông báo lỗi hay gặp.
Percentile tính như JMeter (Apache Commons Math Percentile mặc định: pos = p·(n+1)/100, nội suy tuyến tính).
Throughput = count / (max(timeStamp+elapsed) − min(timeStamp)) như HTML dashboard.

--compare <report-dir>/statistics.json : in chênh lệch từng chỉ số so với HTML report (để chứng minh cách tính khớp).
--exclude-label REGEX : bỏ label (vd setUp đăng ký user) – HTML report KHÔNG bỏ, nên khi so sánh đừng dùng.

Usage: python jtl_stats.py run.jtl [--json stats_truth.json] [--md stats_truth.md] [--compare html/statistics.json]
"""
import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def pct(sorted_vals, p):
    n = len(sorted_vals)
    if n == 0:
        return None
    pos = p * (n + 1) / 100.0
    if pos < 1:
        return float(sorted_vals[0])
    if pos >= n:
        return float(sorted_vals[-1])
    lo = math.floor(pos)
    d = pos - lo
    a, b = sorted_vals[lo - 1], sorted_vals[lo]
    return a + d * (b - a)


def summarize(rows):
    el = sorted(int(r["elapsed"]) for r in rows)
    n = len(el)
    errs = sum(1 for r in rows if r["success"].lower() != "true")
    t0 = min(int(r["timeStamp"]) for r in rows)
    t1 = max(int(r["timeStamp"]) + int(r["elapsed"]) for r in rows)
    span = max((t1 - t0) / 1000.0, 1e-9)
    rb = sum(int(r.get("bytes") or 0) for r in rows)
    sb = sum(int(r.get("sentBytes") or 0) for r in rows)
    return {"sampleCount": n, "errorCount": errs, "errorPct": 100.0 * errs / n, "meanResTime": sum(el) / n,
            "minResTime": el[0], "maxResTime": el[-1], "medianResTime": pct(el, 50), "pct1ResTime": pct(el, 90),
            "pct2ResTime": pct(el, 95), "pct3ResTime": pct(el, 99), "throughput": n / span,
            "receivedKBytesPerSec": rb / 1024.0 / span, "sentKBytesPerSec": sb / 1024.0 / span,
            "start_ms": t0, "end_ms": t1}


def timeline(rows):
    t0 = min(int(r["timeStamp"]) for r in rows)
    buckets = defaultdict(list)
    for r in rows:
        buckets[(int(r["timeStamp"]) - t0) // 60000].append(r)
    out = []
    for m in sorted(buckets):
        rs = buckets[m]
        el = sorted(int(r["elapsed"]) for r in rs)
        out.append({"minute": m, "count": len(rs), "errors": sum(1 for r in rs if r["success"].lower() != "true"),
                    "mean": sum(el) / len(el), "p95": pct(el, 95),
                    "maxThreads": max(int(r.get("allThreads") or 0) for r in rs)})
    return out


KEYS = [("sampleCount", "count", 0), ("errorCount", "errors", 0), ("errorPct", "error %", 2), ("meanResTime", "mean", 2),
        ("minResTime", "min", 0), ("maxResTime", "max", 0), ("medianResTime", "p50", 2), ("pct1ResTime", "p90", 2),
        ("pct2ResTime", "p95", 2), ("pct3ResTime", "p99", 2), ("throughput", "req/s", 3)]


def fmt(v, d):
    return "—" if v is None else (f"{v:.{d}f}" if d else f"{int(round(v))}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jtl", type=Path)
    ap.add_argument("--json", type=Path)
    ap.add_argument("--md", type=Path)
    ap.add_argument("--compare", type=Path)
    ap.add_argument("--exclude-label")
    a = ap.parse_args()
    with open(a.jtl, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows or "elapsed" not in rows[0]:
        raise SystemExit(f"{a.jtl}: không phải jtl CSV có header (cần cột timeStamp, elapsed, label, success…)")
    if a.exclude_label:
        rx = re.compile(a.exclude_label)
        rows = [r for r in rows if not rx.search(r["label"])]
    by = defaultdict(list)
    for r in rows:
        by[r["label"]].append(r)
    stats = {"Total": summarize(rows), **{k: summarize(v) for k, v in sorted(by.items())}}
    errs = Counter((r["label"], r["responseCode"], (r.get("failureMessage") or r.get("responseMessage") or "")[:120])
                   for r in rows if r["success"].lower() != "true")
    res = {"source": str(a.jtl), "rows": len(rows), "percentile_method": "commons-math legacy p(n+1)",
           "statistics": stats, "timeline_per_minute": timeline(rows),
           "top_errors": [{"label": l, "code": c, "message": m, "count": n} for (l, c, m), n in errs.most_common(20)]}
    lines = [f"# stats_truth – `{a.jtl.name}`", "", f"{len(rows)} dòng · percentile: {res['percentile_method']}", "",
             "| Label | " + " | ".join(k[1] for k in KEYS) + " |", "|---|" + "---|" * len(KEYS)]
    for lab, st in stats.items():
        lines.append(f"| {lab} | " + " | ".join(fmt(st[k], d) for k, _, d in KEYS) + " |")
    lines += ["", "## Timeline theo phút", "", "| Phút | count | lỗi | mean | p95 | max threads |", "|---|---|---|---|---|---|"]
    lines += [f"| {t['minute']} | {t['count']} | {t['errors']} | {t['mean']:.1f} | {fmt(t['p95'], 1)} | {t['maxThreads']} |"
              for t in res["timeline_per_minute"]]
    if res["top_errors"]:
        lines += ["", "## Lỗi hay gặp", "", "| Label | code | thông báo | số lần |", "|---|---|---|---|"]
        lines += [f"| {e['label']} | {e['code']} | {e['message'].replace('|', '/')} | {e['count']} |" for e in res["top_errors"]]
    if a.compare:
        ref = json.loads(a.compare.read_text(encoding="utf-8"))
        cmp_rows, worst = [], 0.0
        for lab, st in stats.items():
            r = ref.get(lab)
            if not r:
                cmp_rows.append(f"| {lab} | (không có trong statistics.json) |")
                continue
            for k, name, _ in KEYS:
                mine, theirs = st[k], r.get(k)
                if theirs is None or mine is None:
                    continue
                diff = mine - theirs
                rel = abs(diff) / abs(theirs) * 100 if theirs else (0.0 if diff == 0 else 100.0)
                worst = max(worst, rel)
                cmp_rows.append(f"| {lab} | {name} | {mine:.3f} | {theirs:.3f} | {diff:+.3f} | {rel:.2f}% |")
        missing = [k for k in ref if k not in stats]
        res["compare"] = {"file": str(a.compare), "max_rel_diff_pct": worst, "labels_only_in_report": missing}
        lines += ["", f"## Đối chiếu `{a.compare}`", "", f"Lệch tương đối lớn nhất: **{worst:.2f}%**"
                  + (f" · label chỉ có trong report: {missing}" if missing else ""), "",
                  "| Label | chỉ số | jtl_stats | statistics.json | chênh | % |", "|---|---|---|---|---|---|", *cmp_rows]
        print(f"Đối chiếu statistics.json: lệch tương đối lớn nhất {worst:.2f}%")
    md = "\n".join(lines) + "\n"
    if a.json:
        a.json.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    if a.md:
        a.md.write_text(md, encoding="utf-8")
    if not a.json and not a.md:
        print(md)
    else:
        t = stats["Total"]
        print(f"{len(rows)} dòng · Total: {t['sampleCount']} mẫu, lỗi {t['errorPct']:.2f}%, p95 {fmt(t['pct2ResTime'], 1)} ms, "
              f"{t['throughput']:.2f} req/s")


if __name__ == "__main__":
    main()
