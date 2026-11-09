#!/usr/bin/env python3
"""Xuất checklist.json ra Excel 3 sheet theo mẫu HW01: Test Cases / Checklist / Test Summary Report.

Usage: python build_excel.py <checklist.json> -o <file.xlsx> [--hw HW03] [--tester "Lê Tấn Hiệp – 23120255"]
Cần openpyxl (pip install openpyxl). Không sửa checklist.json.

- Test Cases: mỗi item một dòng (TC ID = id, Objective = mục kiểm tra, Expected, cột kết quả + notes từng nền tảng, Nguồn).
- Checklist: # | IA | Màn hình | Mục kiểm tra | Ưu tiên | P1 | P2 | P3 | Ghi chú — ô kết quả có dropdown.
- Test Summary Report: số item thiết kế/đã chạy/Passed/Failed/N/A/Blocked theo nền tảng (công thức COUNTIF
  trỏ về sheet Checklist), theo IA, theo nguồn.
"""
import argparse, json, sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    sys.exit("Cần openpyxl: python -m pip install openpyxl")

HEAD = Font(bold=True, color="FFFFFF")
FILL = PatternFill("solid", fgColor="1F4E78")
WRAP = Alignment(wrap_text=True, vertical="top")


def header(ws, row, cols, widths=None):
    for c, name in enumerate(cols, 1):
        cell = ws.cell(row=row, column=c, value=name)
        cell.font, cell.fill, cell.alignment = HEAD, FILL, WRAP
        if widths:
            ws.column_dimensions[get_column_letter(c)].width = widths[c - 1]


def result(it, p):
    return "N/A" if p not in it.get("nen_tang", []) else it.get("ket_qua", {}).get(p, "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--hw", default="")
    ap.add_argument("--tester", default="")
    a = ap.parse_args()
    doc = json.loads(Path(a.json).read_text(encoding="utf-8"))
    meta, items = doc["meta"], doc["items"]
    hw = a.hw or meta.get("hw", "")
    plats = list(meta.get("platforms", {}))
    values = meta.get("result_values", ["Passed", "Failed", "N/A", "Blocked"])
    wb = Workbook()

    # --- Test Cases ---
    ws = wb.active
    ws.title = "Test Cases"
    ws["A1"] = f"{hw} – Test Cases: {meta.get('scope', '')}"
    ws["A1"].font = Font(bold=True, size=13)
    ws["A2"] = f"Người thực hiện: {a.tester} · SUT: {meta.get('sut_version', '')}"
    cols = ["TC ID", "HW", "Objective", "IA", "Màn hình", "Precondition", "Căn cứ", "Expected"]
    for p in plats:
        cols += [f"Kết quả {p}", f"Notes {p}"]
    cols += ["Ưu tiên", "Nguồn"]
    header(ws, 4, cols, [9, 7, 36, 8, 18, 30, 30, 60] + [11, 30] * len(plats) + [11, 8])
    for r, it in enumerate(items, 5):
        row = [it["id"], hw, it["muc_kiem_tra"], it["ia"], it["man_hinh"], it.get("tien_dieu_kien", ""),
               it["can_cu"], it["expected"]]
        for p in plats:
            row += [result(it, p), it.get("notes_nt", {}).get(p, "") or it.get("na", {}).get(p, "")]
        row += [it["uu_tien"], it.get("nguon", "")]
        for c, v in enumerate(row, 1):
            ws.cell(row=r, column=c, value=v).alignment = WRAP
    ws.freeze_panes = "B5"

    # --- Checklist ---
    ck = wb.create_sheet("Checklist")
    ck["A1"] = f"{hw} – Checklist GUI: {meta.get('scope', '')}"
    ck["A1"].font = Font(bold=True, size=13)
    ck["A2"] = "Nền tảng: " + "; ".join(f"{k} = {v}" for k, v in meta.get("platforms", {}).items())
    cols = ["#", "IA", "Màn hình", "Mục kiểm tra", "TC tham chiếu", "Ưu tiên"] + plats + ["Ghi chú"]
    header(ck, 4, cols, [5, 8, 20, 44, 10, 11] + [11] * len(plats) + [50])
    dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True)
    ck.add_data_validation(dv)
    first, last = 5, 4 + len(items)
    for r, it in enumerate(items, first):
        notes = "; ".join(f"{p}: {n}" for p, n in it.get("notes_nt", {}).items())
        row = [r - 4, it["ia"], it["man_hinh"], it["muc_kiem_tra"], it["id"], it["uu_tien"]] + \
              [result(it, p) for p in plats] + [notes]
        for c, v in enumerate(row, 1):
            ck.cell(row=r, column=c, value=v).alignment = WRAP
        for c in range(7, 7 + len(plats)):
            dv.add(ck.cell(row=r, column=c))
    ck.freeze_panes = "E5"

    # --- Test Summary Report ---
    sm = wb.create_sheet("Test Summary Report")
    sm["A1"] = f"{hw} – Test Summary Report"
    sm["A1"].font = Font(bold=True, size=13)
    info = [("Phạm vi", meta.get("scope", "")), ("Người kiểm thử", a.tester), ("SUT", meta.get("sut_version", "")),
            ("Căn cứ", meta.get("test_basis", ""))]
    for i, (k, v) in enumerate(info, 3):
        sm.cell(row=i, column=1, value=k).font = Font(bold=True)
        sm.cell(row=i, column=2, value=v).alignment = WRAP
    r0 = 3 + len(info) + 1
    sm.cell(row=r0, column=1, value="1. Kết quả theo nền tảng").font = Font(bold=True)
    header(sm, r0 + 1, ["Chỉ số"] + plats, [26] + [14] * len(plats))
    metrics = [("Item thiết kế", None), ("Đã chạy", "run")] + [(v, v) for v in values] + [("Chưa chạy", "blank")]
    for i, (name, kind) in enumerate(metrics, r0 + 2):
        sm.cell(row=i, column=1, value=name)
        for j, p in enumerate(plats):
            col = get_column_letter(7 + j)
            rng = f"Checklist!{col}{first}:{col}{last}"
            if kind is None:
                f = f"=ROWS({rng})"
            elif kind == "run":
                f = f'=COUNTA({rng})-COUNTIF({rng},"N/A")'
            elif kind == "blank":
                f = f'=COUNTBLANK({rng})'
            else:
                f = f'=COUNTIF({rng},"{kind}")'
            sm.cell(row=i, column=2 + j, value=f)
    r1 = r0 + 2 + len(metrics) + 1
    sm.cell(row=r1, column=1, value="2. Số item theo IA / nguồn").font = Font(bold=True)
    header(sm, r1 + 1, ["Nhóm", "Số item"])
    groups = sorted(Counter(i["ia"] for i in items).items()) + \
        sorted(Counter(f"Căn cứ {i.get('loai_nguon', '')}" for i in items).items()) + \
        sorted(Counter(f"Nguồn {i.get('nguon', '')}" for i in items).items())
    for i, (k, v) in enumerate(groups, r1 + 2):
        sm.cell(row=i, column=1, value=k)
        sm.cell(row=i, column=2, value=v)

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    from openpyxl.workbook.properties import CalcProperties
    wb.calculation = CalcProperties(fullCalcOnLoad=True)  # Excel/LibreOffice tính lại công thức khi mở
    wb.save(a.out)
    print(f"Đã ghi {a.out} ({len(items)} item, {len(plats)} nền tảng)")


if __name__ == "__main__":
    main()
