#!/usr/bin/env python3
"""Kiểm phiếu phiên + tính SUS / SEQ / tỉ lệ hoàn thành / thời gian (schema: references/schema-session.md).

Usage:
  python sus_score.py <sessions-dir> --check                         # chỉ kiểm phiếu
  python sus_score.py <sessions-dir> [--benchmark 05:00] [--expect 7] # in bảng
  python sus_score.py <sessions-dir> --report <report.md> --scope U1 [...]
      → ghi đè nội dung giữa <!-- REPORT:<scope>:usability_sessions:START/END -->
        và <!-- REPORT:<scope>:usability_summary:START/END -->; marker chưa có → in bảng + báo, không tự chèn.

SUS chuẩn (Brooke 1996): câu lẻ (x − 1), câu chẵn (5 − x), tổng × 2,5 → 0–100. Pilot (pilot: true) không tính.
Phiếu thiếu SUS/SEQ → lỗi, không tính phiếu đó (script KHÔNG ước lượng/điền thay). Mã thoát 1 khi có lỗi.
"""
import argparse, json, re, statistics as st, sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

DONE = ["khong_tro_giup", "co_tro_giup", "khong_hoan_thanh"]
LABEL = {"khong_tro_giup": "Hoàn thành, không trợ giúp", "co_tro_giup": "Hoàn thành, có trợ giúp", "khong_hoan_thanh": "Không hoàn thành"}
OPEN = ["ro_rang", "khoi_phuc_loi", "toc_do", "tin_cay"]
MMSS = re.compile(r"^(\d{1,3}):([0-5]\d)$")
PHONE = re.compile(r"\d(?:[ -]?\d){8,}")   # ≥ 9 chữ số, cho phép cách/gạch kiểu SĐT; tiền dùng dấu chấm nên không khớp
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def secs(s):
    m = MMSS.match(s or "")
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def mmss(x):
    x = round(x)
    return f"{x // 60:02d}:{x % 60:02d}"


def sus_score(a):
    return 2.5 * sum((v - 1) if i % 2 == 0 else (5 - v) for i, v in enumerate(a))


def fmt(x, nd=1):
    return "–" if x is None else f"{x:.{nd}f}".replace(".", ",")


def check(path, d, allow):
    err, warn = [], []
    raw = path.read_text(encoding="utf-8")
    for m in PHONE.finditer(raw):
        if len(re.sub(r"\D", "", m.group(0))) >= 9:
            err.append(f"có chuỗi số giống SĐT/số định danh ({m.group(0)[:4]}…) — không đưa dữ liệu cá nhân vào phiếu")
            break
    for m in EMAIL.finditer(raw):
        if m.group(0).lower() not in allow:
            err.append(f"có email ({m.group(0).split('@')[0][:2]}…@…) — dùng mã ẩn danh; email tài khoản test thì thêm --allow")
            break
    if d.get("phien") != path.stem:
        err.append(f"phien = {d.get('phien')!r} khác tên file {path.stem}")
    if not re.fullmatch(r"P\d{1,3}", str(d.get("nguoi_tham_gia") or "")):
        err.append("nguoi_tham_gia phải là mã ẩn danh P01, P02…")
    nv = d.get("nhiem_vu") or {}
    if nv.get("hoan_thanh") not in DONE:
        err.append(f"nhiem_vu.hoan_thanh phải là {'/'.join(DONE)}")
    if secs(nv.get("ket_thuc")) is None:
        err.append("nhiem_vu.ket_thuc thiếu hoặc không phải mm:ss")
    for k, v in (nv.get("moc") or {}).items():
        if v not in (None, "") and secs(v) is None:
            err.append(f"nhiem_vu.moc.{k} = {v!r} không phải mm:ss")
    seq = d.get("seq")
    if not (isinstance(seq, int) and 1 <= seq <= 7):
        err.append(f"seq = {seq!r} — phải là số nguyên 1–7 (thiếu thì hỏi lại người tham gia, không điền thay)")
    sus = d.get("sus")
    if not (isinstance(sus, list) and len(sus) == 10):
        err.append("sus phải có đúng 10 câu")
    else:
        bad = [i + 1 for i, v in enumerate(sus) if not (isinstance(v, int) and 1 <= v <= 5)]
        if bad:
            err.append(f"sus câu {bad} trống hoặc ngoài 1–5 (không điền thay)")
    co = d.get("cau_hoi_mo") or {}
    miss = [k for k in OPEN if co.get(k) in (None, "")]
    if miss:
        warn.append(f"cau_hoi_mo thiếu {miss}")
    for i, e in enumerate(d.get("su_kien") or []):
        if e.get("loai") not in ("L", "D", "N", "T"):
            err.append(f"su_kien[{i}].loai = {e.get('loai')!r} ngoài L/D/N/T")
        if secs(e.get("t")) is None:
            warn.append(f"su_kien[{i}].t không phải mm:ss")
    if nv.get("hoan_thanh") == "khong_tro_giup" and assists(d):
        err.append("có trợ giúp (tro_giup / su_kien T) nhưng hoan_thanh = khong_tro_giup")
    if d.get("reset_du_lieu") is not True and not d.get("pilot"):
        warn.append("reset_du_lieu chưa ghi true")
    return err, warn


def count(d, t):
    return sum(1 for e in d.get("su_kien") or [] if e.get("loai") == t)


def assists(d):
    return max(count(d, "T"), len(d.get("tro_giup") or []))


def stats(xs):
    if not xs:
        return None
    return {"n": len(xs), "mean": st.mean(xs), "sd": st.stdev(xs) if len(xs) > 1 else 0.0,
            "median": st.median(xs), "min": min(xs), "max": max(xs)}


def tables(rows, bench, expect):
    out_s = ["| Phiên | Người TG | Nhóm | Kết quả | Thời gian | Lỗi (L) | Do dự (D) | Trợ giúp | SEQ (1–7) | SUS (0–100) |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out_s.append(f"| {r['phien']} | {r['p']} | {r['nhom'] or '–'} | {LABEL[r['hoan']]} | {mmss(r['t'])} | {r['L']} | {r['D']} | {r['T']} | {r['seq']} | {fmt(r['sus'])} |")
    n = len(rows)
    sus, seq = stats([r["sus"] for r in rows]), stats([r["seq"] for r in rows])
    done = [r for r in rows if r["hoan"] != "khong_hoan_thanh"]
    tm = stats([r["t"] for r in done])
    c = {k: sum(1 for r in rows if r["hoan"] == k) for k in DONE}
    pct = lambda k: f"{k}/{n} ({fmt(100 * k / n, 0)}%)" if n else "–"
    out = ["| Chỉ số | Giá trị |", "|---|---|",
           f"| Số phiên chính tính được | {n}" + (f" / {expect} dự kiến" if expect else "") + " |",
           f"| SUS: trung bình ± SD | {fmt(sus['mean'])} ± {fmt(sus['sd'])} |" if sus else "| SUS | – |",
           f"| SUS: median · min – max | {fmt(sus['median'])} · {fmt(sus['min'])} – {fmt(sus['max'])} |" if sus else None,
           f"| SEQ: trung bình ± SD | {fmt(seq['mean'])} ± {fmt(seq['sd'])} |" if seq else "| SEQ | – |",
           f"| SEQ: median · min – max | {fmt(seq['median'])} · {seq['min']} – {seq['max']} |" if seq else None,
           f"| Hoàn thành, không trợ giúp | {pct(c['khong_tro_giup'])} |",
           f"| Hoàn thành, có trợ giúp | {pct(c['co_tro_giup'])} |",
           f"| Không hoàn thành | {pct(c['khong_hoan_thanh'])} |",
           f"| Tỉ lệ hoàn thành (bất kể trợ giúp) | {pct(len(done))} |"]
    if bench is not None:
        out.append(f"| Hoàn thành trong benchmark {mmss(bench)} | {pct(sum(1 for r in done if r['t'] <= bench))} |")
    if tm:
        out += [f"| Thời gian (phiên hoàn thành): trung bình ± SD | {mmss(tm['mean'])} ± {mmss(tm['sd'])} |",
                f"| Thời gian: median · khoảng | {mmss(tm['median'])} · {mmss(tm['min'])} – {mmss(tm['max'])} |"]
    if n:
        out += [f"| Lỗi / do dự / trợ giúp trung bình mỗi phiên | {fmt(st.mean(r['L'] for r in rows), 2)} / {fmt(st.mean(r['D'] for r in rows), 2)} / {fmt(st.mean(r['T'] for r in rows), 2)} |"]
    out.append("")
    out.append("SUS: câu lẻ (x − 1), câu chẵn (5 − x), tổng × 2,5. SD = độ lệch chuẩn mẫu (n − 1). Pilot không tính. Sinh bằng `sus_score.py`.")
    return "\n".join(out_s) + "\n", "\n".join(x for x in out if x is not None) + "\n"


def put(text, scope, block, body):
    pat = re.compile(rf"(<!-- REPORT:{re.escape(scope)}:{block}:START -->\n)(?:.*?\n)?(<!-- REPORT:{re.escape(scope)}:{block}:END -->)", re.S)
    if not pat.search(text):
        return text, False
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text, count=1), True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--report", type=Path)
    ap.add_argument("--scope", default="U1")
    ap.add_argument("--benchmark", help="mm:ss")
    ap.add_argument("--expect", type=int)
    ap.add_argument("--allow", action="append", default=[], help="email được phép xuất hiện (vd tài khoản test của SUT)")
    a = ap.parse_args()
    allow = {x.lower() for x in a.allow}
    files = sorted(a.dir.glob("S*.json"))
    if not files:
        sys.exit(f"Không có phiếu S*.json trong {a.dir}")
    rows, nerr = [], 0
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"ERROR {f.name}: JSON hỏng – {e}")
            nerr += 1
            continue
        err, warn = check(f, d, allow)
        tag = " (pilot)" if d.get("pilot") else ""
        for e in err:
            print(f"ERROR {f.name}{tag}: {e}")
        for w in warn:
            print(f"WARN  {f.name}{tag}: {w}")
        nerr += len(err)
        if err or d.get("pilot"):
            continue
        rows.append({"phien": d["phien"], "p": d["nguoi_tham_gia"], "nhom": d.get("nhom"), "hoan": d["nhiem_vu"]["hoan_thanh"],
                     "t": secs(d["nhiem_vu"]["ket_thuc"]), "L": count(d, "L"), "D": count(d, "D"), "T": assists(d),
                     "seq": d["seq"], "sus": sus_score(d["sus"])})
    print(f"{len(files)} phiếu, {len(rows)} phiên chính tính được, {nerr} lỗi")
    if a.check:
        sys.exit(1 if nerr else 0)
    bench = secs(a.benchmark) if a.benchmark else None
    t_s, t_sum = tables(rows, bench, a.expect)
    if a.report:
        text = a.report.read_text(encoding="utf-8")
        missing = []
        for block, body in (("usability_sessions", t_s), ("usability_summary", t_sum)):
            text, ok = put(text, a.scope, block, body)
            if not ok:
                missing.append(f"<!-- REPORT:{a.scope}:{block}:START/END -->")
        if missing:
            print("Chưa có marker trong report (không tự chèn): " + ", ".join(missing))
            print(t_s + "\n" + t_sum)
        else:
            a.report.write_text(text, encoding="utf-8")
            print(f"Đã ghi 2 bảng vào {a.report}")
    else:
        print(t_s + "\n" + t_sum)
    sys.exit(1 if nerr else 0)


if __name__ == "__main__":
    main()
