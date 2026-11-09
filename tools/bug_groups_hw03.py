"""Wrapper HW03: nhóm dữ kiện bug G-xx + khung bugs/BUG-<n>.md (chỉ dữ kiện) bằng script tổng quát của skill
`gui-checklist-testing/scripts/bug_groups.py`. File này chỉ giữ dữ liệu riêng HW03 (nhóm SV chốt, môi trường, SUT).

    python tools/bug_groups_hw03.py [--skeleton]       # --skeleton: tạo khung BUG chưa có (không ghi đè file đã có)
"""
import argparse, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(REPO / ".claude" / "skills" / "gui-checklist-testing" / "scripts"))
from failed_list_hw03 import DUP  # noqa: E402
from bug_groups import run  # noqa: E402

ROOT = Path(__file__).resolve().parents[1] / "HW03"
FIRST_BUG = 58   # HW02 dừng ở BUG-57
SUT = "tkob-team/eshop-sut @ de0f48f · web http://localhost:5173 · backend :3000 (CSDL seed lại mỗi lần khởi động)"
ENV = {
    ("P1", "tay"): "P1 – Cốc Cốc 160.0.106 / Windows 11 Home (Asus Vivobook X1505VA) – chạy tay",
    ("P1", "auto"): "P1 – Google Chrome 157.0.8103.39 qua Playwright 1.48.2 (tham chiếu, Q1) / Windows 11",
    ("P2", "tay"): "P2 – Firefox 159.0.1 / Windows 11 – chạy tay",
    ("P2", "auto"): "P2 – Firefox 131.0 bản build của Playwright 1.48.2 / Windows 11",
    ("P3", "tay"): "P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 (adb reverse) – chạy tay",
    ("P3", "auto"): "P3 – Chrome Android 156.0.8078.79 / Android 14, POCO F5 qua Playwright _android",
}
# (mã nhóm, dữ kiện chung quan sát được, [item]) – SV chốt 5/6b: tách G-02, G-23 cũ; bỏ nhóm trùng #160/#165/#167/#169/#170
GROUPS = [
    ("G-01", "Thứ tự Tab không theo vị trí hiển thị (focus bắt đầu ở form, navbar bị đi sau / bỏ qua)", ["CL-10", "CL-12"]),
    ("G-02", "Tiêu đề tab là \"frontend-web\" ở mọi trang", ["CL-13"]),
    ("G-03", "<html lang=\"en\">", ["CL-14"]),
    ("G-04", "Trang không có thẻ <h1>", ["CL-02"]),
    ("G-05", "Ô Email bước 1 Quên mật khẩu: type=\"text\", email sai định dạng vẫn gửi request (phần /login trùng #4)", ["CL-17", "CL-66"]),
    ("G-06", "Nhãn trường bắt buộc thiếu '*' ở Quên mật khẩu B1/B2 và Hồ sơ (phần /login trùng #7)", ["CL-20", "CL-21"]),
    ("G-07", "Lỗi validate chỉ hiện ở hộp thoại trình duyệt (Quên MK B2, Hồ sơ)", ["CL-23"]),
    ("G-08", "Bấm nhãn không focus ô nhập (Đăng nhập, Hồ sơ)", ["CL-38"]),
    ("G-09", "Quên mật khẩu: không có chỉ báo bước", ["CL-24"]),
    ("G-10", "Quên mật khẩu B1: không có 'Quay lại đăng nhập'", ["CL-25"]),
    ("G-11", "Quên mật khẩu B2: không có ô Xác nhận mật khẩu mới", ["CL-26"]),
    ("G-12", "Mã OTP hiển thị 4 chữ số", ["CL-28"]),
    ("G-13", "Quên mật khẩu B2: mật khẩu 'Abcdef1!' bị báo yếu", ["CL-29"]),
    ("G-14", "Quên mật khẩu B2: nút chính và nút phụ giống nhau (G-13 cũ giữ gộp; CL-04 trùng #160 nên còn CL-06)", ["CL-06"]),
    ("G-15", "Hồ sơ: SĐT '912345678' được lưu, thông báo không nêu quy tắc (phần lưu liên quan #97/#113)", ["CL-32"]),
    ("G-16", "Hồ sơ: sau Cập nhật + F5, trường quay về giá trị cũ", ["CL-37"]),
    ("G-17", "Navbar: nút đăng xuất nhãn \"Thoát\"", ["CL-42"]),
    ("G-18", "Navbar: đổi Họ Tên, navbar giữ tên cũ tới khi tải lại", ["CL-56"]),
    ("G-19", "/profile khi chưa đăng nhập: không chuyển, không có link tới Đăng nhập", ["CL-49"]),
    ("G-20", "URL không tồn tại: vùng nội dung trống, không có link về trang chủ", ["CL-50"]),
    ("G-21", "Nút submit không khoá / không có chỉ báo khi bấm nhiều lần (Đăng nhập, Quên MK B1/B2, Hồ sơ)", ["CL-53", "SV-06"]),
    ("G-22", "Lịch sử đơn: không có trạng thái đang tải", ["CL-63"]),
    ("G-23", "Lịch sử đơn: Ngày đặt khác định dạng giữa các nền tảng", ["CL-09"]),
    ("G-24", "Lịch sử đơn: nút 'Hủy đơn' dùng được ở đơn đang giao", ["CL-59"]),
    ("G-25", "Autofill của trình duyệt không điền được (dán được)", ["SV-02"]),
    ("G-26", "Submit thất bại: focus không về ô lỗi", ["SV-03"]),
    ("G-27", "Độ tương phản chữ/nhãn dưới 4.5:1 ở Đăng nhập, Hồ sơ", ["SV-04"]),
    ("G-28", "Link 'Quên mật khẩu?', 'Đăng ký ngay' nhỏ hơn 24×24 px", ["SV-05"]),
]


def cfg():
    return {
        "checklist": str(ROOT / "checklist" / "checklist.json"), "bugs_dir": str(ROOT / "bugs"), "groups_md": str(ROOT / "bugs" / "bug_groups.md"),
        "dup": DUP, "groups": GROUPS, "env": {f"{P}|{k}": v for (P, k), v in ENV.items()}, "sut": SUT, "first_bug": FIRST_BUG,
        "spec_files": [[str(ROOT / "tests" / "C2.spec.ts"), "HW03/tests/C2.spec.ts"]], "image_prefix": "../checklist/", "owner": "SV",
        "title": "# Nhóm dữ kiện bug – T1 checklist C2 (đề xuất, SV xác nhận 🔒)", "generator": "tools/bug_groups_hw03.py",
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--skeleton", action="store_true")
    run(cfg(), ap.parse_args().skeleton)
