"""Điền bảng T1/T3 của HW03 vào report từ checklist.json (không viết lời phân tích).

    python tools/report_t1_hw03.py [--print]

Ghi đè nội dung giữa <!-- REPORT:T1:<khối>:START --> … END --> trong HW03/23120255_HW03_Report.md.
Khối: checklist_summary (mục 3.5), cross_platform (mục 4.1). Marker chưa có → báo, không tự chèn.
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1] / "HW03"
VALS = ["Passed", "Failed", "N/A", "Blocked"]
DIRS = {"P1": "P1_chrome", "P2": "P2_firefox", "P3": "P3_android"}
SCREENS = [("M1", "Đăng nhập"), ("M2", "Quên mật khẩu (B1, B2)"), ("M3", "Hồ sơ"), ("M4", "Lịch sử đơn"), ("M5", "Navbar khi đã đăng nhập")]
M5_REF = {"P1": "P1_M4_1", "P2": "P2_M4_1", "P3": "P3_M3_1"}   # R-M5: dùng lại ảnh có navbar đã đăng nhập


def res(it, P):
    return "N/A" if P not in it.get("nen_tang", []) else it.get("ket_qua", {}).get(P, "")


def cell(s, n=110):
    s = str(s).replace("|", "/").replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


def summary(doc):
    items, plats = doc["items"], list(doc["meta"]["platforms"])
    c = {P: Counter(res(i, P) for i in items) for P in plats}
    src = {P: Counter(i.get("nguon_kq", {}).get(P) for i in items if P in i.get("nen_tang", [])) for P in plats}
    out = ["| Chỉ số | " + " | ".join(f"{P} – {doc['meta']['platforms'][P]}" for P in plats) + " |", "|---|" + "---|" * len(plats)]
    out.append("| Item thiết kế | " + " | ".join(str(len(items)) for _ in plats) + " |")
    out.append("| Đã chạy (trừ N/A) | " + " | ".join(str(len(items) - c[P]["N/A"]) for P in plats) + " |")
    for v in VALS:
        out.append(f"| {v} | " + " | ".join(str(c[P][v]) for P in plats) + " |")
    out.append("| Tỉ lệ Passed / đã chạy | " + " | ".join(f"{100 * c[P]['Passed'] / max(1, len(items) - c[P]['N/A']):.1f}%".replace(".", ",") for P in plats) + " |")
    out.append("| Kết quả từ lượt tay / lượt auto | " + " | ".join(f"{src[P]['tay']} / {src[P]['auto']}" for P in plats) + " |")
    out += ["", "| IA | Số item | " + " | ".join(f"Failed {P}" for P in plats) + " |", "|---|---|" + "---|" * len(plats)]
    for ia in sorted({i["ia"] for i in items}):
        its = [i for i in items if i["ia"] == ia]
        out.append(f"| {ia} | {len(its)} | " + " | ".join(str(sum(res(i, P) == "Failed" for i in its)) for P in plats) + " |")
    runs = sorted({Path(r).name for i in items for r in i.get("run", {}).values() if r})
    out += ["", "Lượt gộp: " + ", ".join(f"`runs/{r}`" for r in runs) + ". Verdict: lượt tay trên trình duyệt thật; item không có trong lượt tay lấy lượt auto (V1, Q1). Sinh bằng `tools/report_t1_hw03.py`."]
    return "\n".join(out) + "\n"


def cross(doc):
    items, plats = doc["items"], list(doc["meta"]["platforms"])
    out = ["**Item có kết quả khác nhau giữa các nền tảng**", "", "| Item | Mục kiểm tra | " + " | ".join(plats) + " | Ghi chú (notes theo nền tảng) |", "|---|---|" + "---|" * len(plats) + "---|"]
    for i in items:
        r = [res(i, P) for P in plats]
        if len({x for x in r if x != "N/A"}) > 1:   # khác nhau thật (bỏ N/A theo thiết kế)
            notes = "; ".join(f"{P}{' (auto)' if i.get('nguon_kq', {}).get(P) == 'auto' else ''}: {cell(re.sub(r'^\[auto – [^\]]*\] (Lỗi: Error: )?', '', i.get('notes_nt', {}).get(P, '')), 90)}"
                              for P in plats if res(i, P) not in ("Passed", "N/A"))
            out.append(f"| {i['id']} | {cell(i['muc_kiem_tra'], 60)} | " + " | ".join(r) + f" | {notes} |")
    out += ["", "**Lệch lượt auto ↔ lượt tay (cùng item, cùng nền tảng) – lấy lượt tay (V1)**", "", "| Item | Nền tảng | Auto | Tay | Nguyên nhân lệch |", "|---|---|---|---|---|"]
    for i in items:
        for P in plats:
            l = i.get("lech_auto_tay", {}).get(P)
            if l:
                out.append(f"| {i['id']} | {P} | {i['auto_status'][P]} | {i['ket_qua'][P]} | {cell(l.split(': ', 1)[-1], 160)} |")
    out += ["", "**Ảnh tổng quan Task 3 (có overlay, `checklist/evidence/`)**", "", "| Màn | " + " | ".join(plats) + " |", "|---|" + "---|" * len(plats)]
    ev = ROOT / "checklist" / "evidence"
    for code, name in SCREENS:
        row = []
        for P in plats:
            if code == "M5":
                f = ev / DIRS[P] / f"{M5_REF[P]}.png"
                row.append(f"dùng lại `{M5_REF[P]}`" + ("" if f.exists() else " (chưa có)"))
            else:
                fs = sorted(x.stem for x in (ev / DIRS[P]).glob(f"{P}_{code}_*.png"))
                row.append(", ".join(f"`{x}`" for x in fs) or "**chưa có**")
        out.append(f"| {code} – {name} | " + " | ".join(row) + " |")
    return "\n".join(out) + "\n"


def put(text, block, body):
    pat = re.compile(rf"(<!-- REPORT:T1:{block}:START -->\n)(?:.*?\n)?(<!-- REPORT:T1:{block}:END -->)", re.S)
    if not pat.search(text):
        return text, False
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text, count=1), True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    doc = json.loads((ROOT / "checklist" / "checklist.json").read_text(encoding="utf-8"))
    blocks = {"checklist_summary": summary(doc), "cross_platform": cross(doc)}
    if a.print:
        for k, v in blocks.items():
            print(f"--- {k}\n{v}")
        return
    rp = ROOT / "23120255_HW03_Report.md"
    text = rp.read_text(encoding="utf-8")
    for k, v in blocks.items():
        text, ok = put(text, k, v)
        print(f"{k}: {'đã ghi' if ok else 'CHƯA CÓ MARKER'}")
    rp.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
