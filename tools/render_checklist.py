"""Render checklist.json (HW03 T1) thành bảng Markdown.

    python tools/render_checklist.py HW03/checklist/checklist.json -o HW03/checklist/checklist.md

Cột kết quả P1/P2/P3 lấy từ item["ket_qua"][Px] nếu có; nền tảng không áp dụng ghi "N/A".
"""
import argparse, json
from collections import Counter
from pathlib import Path

IA_NAMES = {
    "IA-01": "General UI standards",
    "IA-02": "Forms",
    "IA-03": "Navigation",
    "IA-04": "Feedback / state",
}


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", "<br>")


def result(it, p):
    if p not in it.get("nen_tang", []):
        return "N/A"
    return it.get("ket_qua", {}).get(p, "")


def render(doc):
    meta, items = doc["meta"], doc["items"]
    plats = list(meta.get("platforms", {}))
    out = [f"# Checklist GUI – {meta.get('scope', '')}", ""]
    out.append(f"> Sinh tự động từ `checklist.json` bằng `tools/render_checklist.py` — không sửa tay. Phiên bản: {meta.get('version', '')}.")
    out.append("")
    out.append(f"- SUT: {meta.get('sut_version', '')}")
    out.append(f"- Căn cứ: {meta.get('test_basis', '')}")
    out.append("- Nền tảng: " + "; ".join(f"{k} = {v}" for k, v in meta.get("platforms", {}).items()))
    out.append("")

    by_ia = Counter(i["ia"] for i in items)
    by_src = Counter(i.get("loai_nguon", "") for i in items)
    by_origin = Counter(i.get("nguon", "") for i in items)
    out += ["## Thống kê", "",
            "| IA | Số item |", "|---|---|"]
    out += [f"| {ia} {IA_NAMES.get(ia, '')} | {by_ia[ia]} |" for ia in sorted(by_ia)]
    out.append(f"| **Tổng** | **{len(items)}** |")
    out.append("")
    out.append("Loại căn cứ: " + ", ".join(f"{k} {v}" for k, v in sorted(by_src.items())) +
               " · Nguồn item: " + ", ".join(f"{k} {v}" for k, v in sorted(by_origin.items())) +
               " · Ưu tiên: " + ", ".join(f"{k} {v}" for k, v in sorted(Counter(i['uu_tien'] for i in items).items())))
    out.append("")

    if doc.get("assumptions"):
        out += ["## Giả định", "", "| Mã | Nội dung |", "|---|---|"]
        out += [f"| {k} | {cell(v)} |" for k, v in doc["assumptions"].items()]
        out.append("")

    for ia in sorted(by_ia):
        out += [f"## {ia} – {IA_NAMES.get(ia, '')}", ""]
        head = ["ID", "Màn hình", "Mục kiểm tra", "Căn cứ", "Expected (ngưỡng Pass/Fail)", "Ưu tiên", "Nguồn"] + plats + ["Notes"]
        out.append("| " + " | ".join(head) + " |")
        out.append("|" + "---|" * len(head))
        for it in items:
            if it["ia"] != ia:
                continue
            exp = it["expected"]
            if it.get("tien_dieu_kien"):
                exp = f"*Tiền điều kiện:* {it['tien_dieu_kien']}<br>{exp}"
            notes = []
            if it.get("gia_dinh"):
                notes.append(it["gia_dinh"])
            for p, why in it.get("na", {}).items():
                notes.append(f"{p} N/A – {why}")
            if it.get("notes"):
                notes.append(it["notes"])
            row = [it["id"], it["man_hinh"], it["muc_kiem_tra"], f"{it['can_cu']} · *{it.get('loai_nguon', '')}*",
                   exp, it["uu_tien"], it.get("nguon", "")] + [result(it, p) for p in plats] + ["<br>".join(notes)]
            out.append("| " + " | ".join(cell(c) for c in row) + " |")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    doc = json.loads(Path(a.json).read_text(encoding="utf-8"))
    ids = [i["id"] for i in doc["items"]]
    assert len(ids) == len(set(ids)), "trùng id"
    md = render(doc)
    out = Path(a.out) if a.out else Path(a.json).with_suffix(".md")
    out.write_text(md + "\n", encoding="utf-8")
    print(f"Đã ghi {out} ({len(ids)} item)")


if __name__ == "__main__":
    main()
