"""Sinh HW03/bugs/failed_list.md: mọi item Failed (item × nền tảng) từ checklist.json + đối chiếu trùng với
issue nhóm (HW03/bugs/issues.json, lấy bằng `gh issue list --repo tkob-team/eshop-sut --state all --json ...`)
và BUG-xx HW02 của SV (BUG-01…14 = #17–30, BUG-15…57 = #161–203).

    python tools/failed_list_hw03.py

DUP do AI đối chiếu theo tiêu đề issue + màn hình + notes; SV xác nhận trước khi viết bug (T1 bước 6).
Chỉ nêu mã issue/màn, không mô tả bug.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "HW03"
HW02 = {**{17 + k: f"BUG-{k + 1:02d}" for k in range(14)}, **{161 + k: f"BUG-{k + 15:02d}" for k in range(43)}}
# (loại, [issue], ghi chú đối chiếu). loại: TRÙNG = cùng màn + cùng lỗi; MỘT PHẦN = issue phủ một màn, màn khác chưa có issue;
# LIÊN QUAN = cùng kiểu lỗi nhưng khác màn → vẫn tính MỚI
DUP = {
    "CL-01": ("TRÙNG", [9], "notes cả 3 nền tảng chỉ nêu chuỗi tiếng Anh ở Đăng nhập (\"Username\", \"Sign In\")"),
    "CL-03": ("TRÙNG", [9], "tiêu đề form Đăng nhập là \"Đăng Ký\""),
    "CL-16": ("TRÙNG", [122], "cùng lời chào navbar; HW02 BUG-11/#27 là XSS ở Đăng ký (nguồn dữ liệu khác)"),
    "CL-17": ("MỘT PHẦN", [4], "#4 phủ /login; /forgot-password bước 1 chưa có issue"),
    "CL-66": ("MỘT PHẦN", [4], "#4 (không kiểm tra định dạng) phủ /login; /forgot-password chưa có issue"),
    "CL-18": ("TRÙNG", [9], "nhãn \"Username\""),
    "CL-19": ("TRÙNG", [5], "chỉ /login fail; bước 2 Quên MK đạt (notes auto)"),
    "CL-20": ("MỘT PHẦN", [7], "#7 phủ /login; Quên MK bước 1/2 chưa có issue"),
    "CL-22": ("TRÙNG", [6], ""),
    "CL-31": ("TRÙNG", [111, 112], "Web từ chối SĐT 10/11 số đầu 0"),
    "CL-32": ("MỘT PHẦN", [97, 113], "#97 (API lưu SĐT 9 số), #113 (Web nhận đầu khác 0); phần thông báo không nêu quy tắc chưa có issue"),
    "CL-41": ("TRÙNG", [166], "badge Giỏ hàng trên navbar (HW02 của SV)"),
    "CL-52": ("TRÙNG", [1, 2, 3], "bộ đếm +2, khoá từ lần 2, khoá 180 s"),
    "CL-04": ("LIÊN QUAN", [160], "#160 là nút Mobile; nút C2 trên Web chưa có issue"),
    "CL-08": ("LIÊN QUAN", [170], "#170 là 'VND' ở trang chủ; Lịch sử đơn chưa có issue"),
    "CL-26": ("LIÊN QUAN", [30], "#30 là form Đăng ký; Quên MK bước 2 chưa có issue"),
    "CL-29": ("LIÊN QUAN", [17], "#17 cùng thông báo \"Mật khẩu quá yếu!\" ở Đăng ký; Quên MK bước 2 chưa có issue"),
    "CL-37": ("LIÊN QUAN", [111, 123], "SV xem: trường quay về giá trị cũ sau F5, có thể do #111 chặn lưu hoặc #123"),
    "CL-40": ("LIÊN QUAN", [169], "#169 là trang Giỏ; /profile chưa có issue"),
    "CL-60": ("LIÊN QUAN", [165], "#165 là xoá dòng giỏ; huỷ đơn chưa có issue"),
    "CL-62": ("LIÊN QUAN", [167], "#167 là giỏ trống; Lịch sử đơn trống chưa có issue"),
}


def main():
    doc = json.loads((ROOT / "checklist" / "checklist.json").read_text(encoding="utf-8"))
    issues = {i["number"]: i for i in json.loads((ROOT / "bugs" / "issues.json").read_text(encoding="utf-8"))}
    plats = list(doc["meta"]["platforms"])
    rows, n, harness, pend, excl = [], {"TRÙNG": 0, "MỘT PHẦN": 0, "MỚI": 0}, [], 0, []
    cells = {P: 0 for P in plats}
    for it in doc["items"]:
        f = [P for P in plats if it.get("ket_qua", {}).get(P) == "Failed"]
        if not f:
            continue
        for P in f:
            cells[P] += 1
        kind, nums, note = DUP.get(it["id"], ("MỚI", [], ""))
        bad = [x for x in nums if x not in issues]
        if bad:
            raise SystemExit(f"{it['id']}: issue {bad} không có trong issues.json")
        nobug = [P for P in f if it.get("lap_bug", {}).get(P) is False]
        if nobug == f:   # mọi ô Failed đều bị quyết định loại khỏi lập bug
            excl.append(it["id"])
            rows.append(f"| {len(rows) + 1} | {it['id']} | {it['man_hinh']} | {it['muc_kiem_tra'].replace('|', '/')} | {', '.join(f)} | "
                        f"{'/'.join(sorted({it.get('nguon_kq', {}).get(P, '?') for P in f}))} | loại khỏi lập bug (5/6a) | {note or 'xem notes'} |")
            continue
        refs = ", ".join(f"#{x}" + (f" ({HW02[x]})" if x in HW02 else "") for x in nums)
        col = {"TRÙNG": f"trùng {refs}", "MỘT PHẦN": f"trùng một phần {refs} + MỚI", "LIÊN QUAN": f"**MỚI** (liên quan {refs})"}.get(kind, "**MỚI**")
        n["MỚI" if kind == "LIÊN QUAN" else kind] += 1
        src = "/".join(sorted({it.get("nguon_kq", {}).get(P, "?") for P in f}))
        # ô auto Failed chỉ vì lỗi harness (Timeout, không có assertion nào fail) → chưa cô lập nguyên nhân, cần chạy lại
        hx = [P for P in f if it.get("nguon_kq", {}).get(P) == "auto" and "TimeoutError" in it.get("notes_nt", {}).get(P, "")
              and "Lỗi: Error:" not in it.get("notes_nt", {}).get(P, "")]
        if hx:
            harness.append(f"{it['id']} {'/'.join(hx)}")
            note = (note + "; " if note else "") + f"⚠ {'/'.join(hx)}: Failed do TimeoutError của Playwright, chưa có assertion fail → chạy lại trước khi coi là lỗi"
            if hx == f:
                col += " ⚠ chờ chạy lại"
                pend += 1
        rows.append(f"| {len(rows) + 1} | {it['id']} | {it['man_hinh']} | {it['muc_kiem_tra'].replace('|', '/')} | {', '.join(f)} | {src} | {col} | {note} |")
    out = [
        "# Danh sách Failed – T1 checklist C2 (sinh bằng `tools/failed_list_hw03.py` từ `checklist.json`)",
        "",
        f"{len(rows)} item Failed · ô Failed theo nền tảng: " + ", ".join(f"{P} {cells[P]}" for P in plats) + f" (tổng {sum(cells.values())}).",
        f"Đối chiếu `HW03/bugs/issues.json` ({len(issues)} issue nhóm, tới #{max(issues)}) và BUG-01…57 HW02 của em: "
        f"**trùng {n['TRÙNG']}**, **trùng một phần {n['MỘT PHẦN']}** (màn còn lại là MỚI), **MỚI {n['MỚI']}**; loại khỏi lập bug: {', '.join(excl) or 'không'} (quyết định 5/6a).",
        "CL-30, CL-48 trên P3 = Blocked (T-P3: Playwright timeout) nên không còn trong danh sách.",
        "",
        "Cột *kết quả từ*: `tay` = lượt chạy tay trên trình duyệt thật; `auto` = lượt Playwright (P1 Chrome 157 tham chiếu – Q1; P2 Firefox 131 của Playwright; P3 Chrome Android thật). "
        "Đối chiếu trùng do AI làm theo tiêu đề issue + màn hình + notes; **SV xác nhận** trước khi viết BUG-58… (T1 bước 6). Mỗi item = một ứng viên bug, chưa phải bug.",
        "",
        "| # | Item | Màn hình | Mục kiểm tra | Failed trên | Kết quả từ | Issue trùng / MỚI | Ghi chú đối chiếu |",
        "|---|---|---|---|---|---|---|---|",
        *rows,
        "",
    ]
    (ROOT / "bugs" / "failed_list.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(rows)} item, ô {cells}, {n}, loại: {excl}, timeout harness: {harness}")


if __name__ == "__main__":
    main()
