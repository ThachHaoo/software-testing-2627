"""Sinh HW03/bugs/failed_list.md: mọi item Failed (item × nền tảng) từ checklist.json + đối chiếu trùng với
issue nhóm (HW03/bugs/issues.json, lấy bằng `gh issue list --repo tkob-team/eshop-sut --state all --json ...`)
và BUG-xx HW02 của SV (BUG-01…14 = #17–30, BUG-15…57 = #161–203).

    python tools/failed_list_hw03.py

Wrapper: dữ liệu đối chiếu riêng HW03 ở đây; code ở skill `gui-checklist-testing/scripts/failed_list.py`.

DUP do AI đối chiếu theo tiêu đề issue + màn hình + notes; SV xác nhận trước khi viết bug (T1 bước 6).
Chỉ nêu mã issue/màn, không mô tả bug.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / ".claude" / "skills" / "gui-checklist-testing" / "scripts"))
from failed_list import run  # noqa: E402

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
    "CL-04": ("TRÙNG", [160], "SV chốt trùng (5/6b): #160 nút tích cực màu xanh lá"),
    "CL-08": ("TRÙNG", [170], "SV chốt trùng (5/6b): #170 định dạng tiền"),
    "CL-26": ("LIÊN QUAN", [30], "#30 là form Đăng ký; Quên MK bước 2 chưa có issue"),
    "CL-29": ("LIÊN QUAN", [17], "#17 cùng thông báo \"Mật khẩu quá yếu!\" ở Đăng ký; Quên MK bước 2 chưa có issue"),
    "CL-37": ("LIÊN QUAN", [111, 123], "SV xem: trường quay về giá trị cũ sau F5, có thể do #111 chặn lưu hoặc #123"),
    "CL-40": ("TRÙNG", [169], "SV chốt trùng (5/6b): #169 navbar không highlight trang hiện tại"),
    "CL-60": ("TRÙNG", [165], "SV chốt trùng (5/6b): #165 thao tác huỷ/xoá không có hộp xác nhận"),
    "CL-62": ("TRÙNG", [167], "SV chốt trùng (5/6b): #167 empty state không có hình minh hoạ"),
}



def cfg():
    return {
        "checklist": str(ROOT / "checklist" / "checklist.json"), "issues": str(ROOT / "bugs" / "issues.json"),
        "issues_label": "HW03/bugs/issues.json", "out": str(ROOT / "bugs" / "failed_list.md"),
        "dup": DUP, "issue_alias": HW02, "compare_label": "BUG-01…57 HW02 của em", "exclude_note": "5/6a",
        "title": "# Danh sách Failed – T1 checklist C2 (sinh bằng `tools/failed_list_hw03.py` từ `checklist.json`)",
        "extra_lines": ["CL-30, CL-48 trên P3 = Blocked (T-P3: Playwright timeout) nên không còn trong danh sách."],
        "source_note": "Cột *kết quả từ*: `tay` = lượt chạy tay trên trình duyệt thật; `auto` = lượt Playwright (P1 Chrome 157 tham chiếu – Q1; P2 Firefox 131 của Playwright; P3 Chrome Android thật). "
                       "Đối chiếu trùng do AI làm theo tiêu đề issue + màn hình + notes; **SV xác nhận** trước khi viết BUG-58… (T1 bước 6). Mỗi item = một ứng viên bug, chưa phải bug.",
    }


def main():
    run(cfg())


if __name__ == "__main__":
    main()
