#!/usr/bin/env python3
"""Bước 6 – gộp kết quả các lượt chạy (mỗi trình duyệt một report) của một feature.

Đọc results.json (Playwright JSON reporter, cạnh index.html trong HW04/reports/<project>_<ts>/),
lấy test có tiêu đề bắt đầu bằng tc_id trong data/<X_FRnn>.json, rồi ghi:
  <feature-dir>/results.md     bảng tc_id × trình duyệt (Pass / Fail / Blocked / Not run) + tổng
  <feature-dir>/bug_groups.md  TC Fail gom theo triệu chứng GIỐNG HỆT (cùng tập assertion lỗi + cùng giá trị nhận được).
                               Mỗi TC: Expected (data), Actual (nguyên văn assertion lỗi), trình duyệt, yêu cầu bị vi phạm,
                               vị trí code SUT, bug/issue HW02 (từ --context). CHỈ dữ kiện — SV viết bug.
  <feature-dir>/evidence/<TC>_<project>.png  ảnh lỗi tách từ HTML report (--evidence)

Quy tắc verdict:
  passed → Pass · failed có lỗi assertion (expect) → Fail
  failed/timedOut mà lỗi chỉ là TimeoutError (không assertion nào fail) → Blocked (lỗi harness)
  skipped kèm annotation type 'blocked' → Blocked · skipped khác → Not run

--context: JSON {"<HW02 bug_id>": {"issue": "...", "requirements": [...], "code": [...], "source": "..."}} — dữ kiện
           do AI trích từ HW02/bugs và mã SUT (ghi nguồn), không phải nhận định.

Usage: python merge_reports.py HW04/data/A_FR01.json HW04/A_FR01 <report chrome> <report edge> <report firefox> \
           [--context HW04/A_FR01/bug_context.json] [--evidence]
"""
import argparse
import base64
import io
import json
import re
import shutil
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ANSI = re.compile(r"\x1b\[[0-9;]*m")
TS = re.compile(r"\d{10,}")


def walk(suite, out):
    for s in suite.get("suites", []):
        walk(s, out)
    for sp in suite.get("specs", []):
        for t in sp.get("tests", []):
            out.append((sp["title"], t))


def clean(msg: str) -> str:
    """Nguyên văn thông điệp assertion, bỏ call log và khung mã nguồn (phần của Playwright, không phải Actual)."""
    out = []
    for line in ANSI.sub("", msg).splitlines():
        if line.startswith("Call log:") or re.match(r"^\s*>?\s*\d+ \|", line):
            break
        out.append(line.rstrip())
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out)


def signature(errs: list[str]) -> tuple:
    """Triệu chứng: dòng tiêu đề assertion + giá trị nhận được (Received / dòng '+' của diff), số dài (ts) chuẩn hoá."""
    sig = []
    for e in errs:
        lines = e.splitlines()
        head = [l for l in lines[:3] if l.strip() and not l.startswith(("Expected", "Received", "-", "+"))]
        recv = [l.strip() for l in lines if l.startswith("Received") or (l.startswith("+") and not l.startswith("+ Received"))]
        sig.append(TS.sub("{ts}", " | ".join(head + recv)))
    return tuple(sorted(sig))


def verdict(test) -> tuple[str, list[str]]:
    r = (test.get("results") or [{}])[-1]
    st = r.get("status", "skipped")
    errs = [clean(e.get("message", "")) for e in r.get("errors", []) if e.get("message", "").strip()]
    if st == "passed":
        return "Pass", []
    if st == "skipped":
        ann = [a for a in test.get("annotations", []) + r.get("annotations", []) if a.get("type") == "blocked"]
        return ("Blocked", [ann[0].get("description", "")]) if ann else ("Not run", [])
    has_assert = any("expect(" in e for e in errs)
    if st == "timedOut" or (errs and not has_assert and all("Timeout" in e.splitlines()[0] for e in errs)):
        return "Blocked", errs or ["timeout"]
    return "Fail", errs


def screenshots(report: Path, extra: bool = False) -> dict:
    """tiêu đề test → ảnh screenshot cuối cùng trong HTML report (dữ liệu nhúng trong index.html).
    extra=True: tiêu đề test → [(tên attachment, ảnh)] của ảnh do spec tự đính (tên chứa '_after-', vd <TC>_after-action)."""
    html = (report / "index.html").read_text(encoding="utf-8")
    m = re.search(r"base64,(UEsDB[A-Za-z0-9+/=]+)", html)
    if not m:
        return {}
    z = zipfile.ZipFile(io.BytesIO(base64.b64decode(m.group(1))))
    out = {}
    for n in z.namelist():
        if n == "report.json":
            continue
        for t in json.loads(z.read(n)).get("tests", []):
            atts = [a for r in t.get("results", []) for a in r.get("attachments", []) if a.get("path")]
            if extra:
                ex = [(a["name"], report / a["path"]) for a in atts if "_after-" in a.get("name", "")]
                if ex:
                    out[t["title"]] = ex
                continue
            shots = [a["path"] for a in atts if a.get("name") == "screenshot"]
            if shots:
                out[t["title"]] = report / shots[-1]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data", type=Path)
    ap.add_argument("feature_dir", type=Path)
    ap.add_argument("reports", nargs="+", type=Path)
    ap.add_argument("--context", type=Path)
    ap.add_argument("--evidence", action="store_true")
    a = ap.parse_args()
    data = json.loads(a.data.read_text(encoding="utf-8"))
    cases = {t["tc_id"]: t for t in data["testcases"]}
    ids = list(cases)
    ctx = json.loads(a.context.read_text(encoding="utf-8")) if a.context else {}
    table = defaultdict(dict)       # tc_id -> project -> (verdict, errs)
    runs, shots, extras = [], {}, {}
    for rep in a.reports:
        rj = json.loads((rep / "results.json").read_text(encoding="utf-8"))
        project = rep.name.rsplit("_", 1)[0]
        runs.append((project, rep.as_posix(), rj.get("config", {}).get("metadata", {}).get("Run by", "")))
        tests = []
        for s in rj.get("suites", []):
            walk(s, tests)
        for title, t in tests:
            tc = next((i for i in ids if title.startswith(i + " ")), None)
            if tc:
                table[tc][project] = verdict(t)
        if a.evidence:
            for title, p in screenshots(rep).items():
                tc = next((i for i in ids if title.startswith(i + " ")), None)
                if tc:
                    shots[(tc, project)] = p
            for title, lst in screenshots(rep, extra=True).items():
                tc = next((i for i in ids if title.startswith(i + " ")), None)
                if tc:
                    extras[(tc, project)] = lst
    projects = [p for p, _, _ in runs]

    # results.md
    L = [f"# {data['feature']} – kết quả chạy đa trình duyệt", "",
         "| trình duyệt | report | Run by |", "|---|---|---|"]
    L += [f"| {p} | `{r}` | {rb} |" for p, r, rb in runs]
    L += ["", "| tc_id | loại | HW02 | " + " | ".join(projects) + " |", "|---|---|---|" + "---|" * len(projects)]
    tot = defaultdict(lambda: defaultdict(int))
    for i in ids:
        row = []
        for p in projects:
            v = table[i].get(p, ("Not run", []))[0]
            tot[p][v] += 1
            row.append(v)
        L.append(f"| {i} | {cases[i]['type']} | {cases[i]['hw02']['status']} | " + " | ".join(row) + " |")
    L += ["", "| tổng | " + " | ".join(projects) + " |", "|---|" + "---|" * len(projects)]
    for v in ("Pass", "Fail", "Blocked", "Not run"):
        L.append(f"| {v} | " + " | ".join(str(tot[p][v]) for p in projects) + " |")
    (a.feature_dir / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")

    # evidence
    ev_dir = a.feature_dir / "evidence"
    copied = {}
    copied_extra = {}      # (tc, project) -> [ảnh do spec tự đính: <TC>_after-*]
    if a.evidence:
        ev_dir.mkdir(exist_ok=True)
        for (tc, p), src in shots.items():
            if table[tc].get(p, ("",))[0] in ("Fail", "Blocked") and src.is_file():
                dst = ev_dir / f"{tc}_{p}.png"
                shutil.copy2(src, dst)
                copied[(tc, p)] = dst
        for (tc, p), lst in extras.items():
            if table[tc].get(p, ("",))[0] in ("Fail", "Blocked"):
                for name, src in lst:
                    if src.is_file():
                        dst = ev_dir / f"{name}_{p}.png"
                        shutil.copy2(src, dst)
                        copied_extra.setdefault((tc, p), []).append(dst)

    # bug_groups.md
    groups = defaultdict(list)      # signature -> [(tc, project, errs)]
    for i in ids:
        for p in projects:
            v, errs = table[i].get(p, ("Not run", []))
            if v == "Fail":
                groups[signature(errs)].append((i, p, errs))
    G = [f"# {data['feature']} – nhóm TC Fail (dữ kiện, SV viết bug)", "",
         "Nhóm = cùng tập assertion lỗi và cùng giá trị nhận được (triệu chứng giống hệt; số dài `{ts}` chuẩn hoá).",
         "Không đặt tên bug, không severity/priority, không kết luận nguyên nhân, không đề xuất gộp/tách.",
         "Ảnh lúc kết thúc = screenshot Playwright chụp lúc test KẾT THÚC (screenshot: 'only-on-failure'), không phải lúc assertion đầu tiên lỗi.",
         "Ảnh ngay sau thao tác chính = ảnh spec tự đính (`<TC>_after-submit` / `<TC>_after-action[-k]`) ngay sau bấm Đăng Ký / Thêm / Xoá.", ""]
    for n, (sig, items) in enumerate(sorted(groups.items(), key=lambda x: (-len(x[1]), x[1][0][0])), 1):
        tcs = list(dict.fromkeys(i for i, _, _ in items))
        G += [f"## G{n} – {len(tcs)} TC × {len(items) // max(len(tcs), 1)} trình duyệt ({len(items)} lượt Fail)", "",
              "Assertion lỗi (chung của nhóm):", ""]
        G += [f"- `{s}`" for s in sig]
        G.append("")
        for tc in tcs:
            c = cases[tc]
            br = [p for i, p, _ in items if i == tc]
            bug = c["hw02"].get("bug_id", "")
            info = ctx.get(bug, {})
            G += [f"### {tc} – {c['title']}", "",
                  f"- Trình duyệt Fail: {', '.join(br)}",
                  f"- Loại / kỹ thuật: {c['type']} / {c['technique']} {c.get('bva_point', '')}".rstrip(),
                  f"- HW02: {c['hw02']['status']}" + (f" · {bug}" if bug else "") + (f" · issue {info['issue']}" if info.get("issue") else ""),
                  f"- Expected (HW02, nguyên văn): {c['expected']}"]
            if info.get("requirements"):
                G.append("- Yêu cầu bị vi phạm (theo " + info.get("source", bug) + "): " + "; ".join(info["requirements"]))
            if info.get("code"):
                G.append("- Vị trí code SUT: " + "; ".join(info["code"]))
            ev = [f"`{copied[(tc, p)].relative_to(a.feature_dir).as_posix()}`" for p in br if (tc, p) in copied]
            if ev:
                G.append("- Ảnh lúc kết thúc: " + ", ".join(ev))
            evx = [f"`{d.relative_to(a.feature_dir).as_posix()}`" for p in br for d in copied_extra.get((tc, p), [])]
            if evx:
                G.append("- Ảnh ngay sau thao tác chính: " + ", ".join(evx))
            errs = next(e for i, p, e in items if i == tc)
            G += [f"- Actual ({br[0]}, nguyên văn assertion lỗi):", "", "```"] + ["\n\n".join(errs)] + ["```", ""]
    if not groups:
        G.append("Không có TC Fail.")
    (a.feature_dir / "bug_groups.md").write_text("\n".join(G) + "\n", encoding="utf-8", newline="\n")
    print(f"Đã ghi {a.feature_dir / 'results.md'}, bug_groups.md ({len(groups)} nhóm), {len(copied)} ảnh lúc kết thúc + {sum(map(len, copied_extra.values()))} ảnh sau thao tác")


if __name__ == "__main__":
    main()
