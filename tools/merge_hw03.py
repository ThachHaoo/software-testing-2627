"""Wrapper HW03: gộp lượt auto + tay của T1 vào HW03/checklist/checklist.json bằng script tổng quát của skill
`gui-checklist-testing/scripts/merge_runs.py` (quyết định V1, Q1, Q2, T-P3… trong report_plan mục e).

    python tools/merge_hw03.py [--dry-run]

File này chỉ giữ dữ liệu riêng HW03 (tên file lượt, môi trường auto, nguyên nhân lệch, quyết định override).
"""
import argparse, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / ".claude" / "skills" / "gui-checklist-testing" / "scripts"))
from merge_runs import run  # noqa: E402

CL = REPO / "HW03" / "checklist"
DIRS = {"P1": "P1_chrome", "P2": "P2_firefox", "P3": "P3_android"}
AUTO = {"P1": "P1_auto_20261109-2236.json", "P2": "P2_auto_20261109-2240.json", "P3": "P3_auto_20261109-2244.json"}
MANUAL = {"P1": "P1_manual_20261109-2257", "P2": "P2_manual_20261110-0010", "P3": "P3_manual_20261110-0046"}
AUTO_ENV = {"P1": "Chrome 157 qua Playwright (Q1: P1 chính thức là Cốc Cốc 160, cùng nhân Chromium)",
            "P2": "Firefox 131 bản build của Playwright", "P3": "Chrome Android 156 thật trên POCO F5 (Playwright _android)"}
LOCALE = "auto ép locale vi-VN (playwright.config) nên hiện \"6.000.000 ₫\"; trình duyệt thật của SV theo locale máy hiện \"6,000,000 ₫\""
CAUSE = {  # nguyên nhân lệch, dữ kiện từ run_check.md mục 1c (L1–L8)
    ("CL-08", "P2"): LOCALE, ("CL-08", "P3"): LOCALE,
    ("CL-08", "P1"): "auto chấm riêng từng nền tảng (P1 thấy \"6.000.000 ₫\", đạt ngưỡng ký hiệu + phân cách); Failed do so kiểu phân cách giữa P1/P2/P3 theo R9=b (override)",
    ("CL-09", "P1"): "cả hai cùng thấy \"9/11/2026\" (ảnh P1_CL-09_1); khác ở cách chấm ngưỡng dd/mm/yyyy (run_check R11)",
    ("CL-11", "P1"): "auto so toạ độ, bố cục 2 cột nên 'Cập nhật' → 'Hủy đơn' bị tính là nhảy ngược; SV đọc chuỗi Tab theo cột/hàng",
    ("CL-11", "P2"): "auto so toạ độ, bố cục 2 cột nên 'Cập nhật' → 'Hủy đơn' bị tính là nhảy ngược; SV đọc chuỗi Tab theo cột/hàng",
    ("CL-15", "P1"): "auto đo ở viewport 375 px: scrollWidth 381 > 375; lượt tay không đo ở đúng 375 px (ảnh chụp cửa sổ hẹp, không thấy thanh cuộn)",
    ("CL-15", "P2"): "auto đo ở viewport 375 px: scrollWidth 382 > 375; lượt tay không đo ở đúng 375 px (ảnh chụp cửa sổ hẹp, không thấy thanh cuộn)",
    ("SV-02", "P1"): "auto chỉ kiểm vế dán (Ctrl+V); vế autofill kiểm tay",
}
# Quyết định 5/6a (report_plan mục e: T-P3, CL-34, CL-52 P3) và 4/6c (R9, R11). Áp sau cùng → chạy lại script vẫn giữ.
# ket_qua: đổi kết quả; them: nối vào notes (không sửa chữ SV); lap_bug False: loại khỏi danh sách lập bug.
OVERRIDE = {
    ("CL-30", "P3"): {"ket_qua": "Blocked", "them": "Blocked (T-P3): Playwright TimeoutError, không có assertion fail – không lập bug", "lap_bug": False},
    ("CL-48", "P3"): {"ket_qua": "Blocked", "them": "Blocked (T-P3): Playwright TimeoutError, không có assertion fail – không lập bug", "lap_bug": False},
    ("CL-34", "P2"): {"them": "chỉ Firefox Playwright, chưa xác nhận trên trình duyệt thật – không lập bug (5/6a)", "lap_bug": False},
    ("CL-08", "P1"): {"ket_qua": "Failed", "them": "SV chốt R9=b: Expected \"cùng một kiểu phân cách trên cả 3 nền tảng\" áp cho cả P1; P1 hiện \"30.000.000 ₫\", P2/P3 hiện \"6,000,000 ₫\" → kiểu phân cách khác nhau giữa các nền tảng (lý do lấy từ khuyến nghị run_check R9, SV có thể sửa)"},
    ("CL-09", "P1"): {"ket_qua": "Failed", "them": "SV chốt R11=b: Expected \"dd/mm/yyyy và giống nhau trên P1, P2, P3\" áp cho cả P1; ảnh P1_CL-09_1 hiện \"9/11/2026\" (ngày 1 chữ số, không phải dd/mm/yyyy), P2/P3 hiện \"11/9/2026\" → khác nhau giữa các nền tảng (lý do lấy từ khuyến nghị run_check R11, SV có thể sửa)"},
    ("CL-52", "P3"): {"them": "thiếu ảnh (ảnh P3_CL-52_1 chỉ thấy \"Đăng nhập thất bại\", không thấy trạng thái khoá) – 5/6a"},
}


def cfg():
    return {"checklist": str(CL / "checklist.json"), "runs_dir": str(CL / "runs"), "evidence_dir": str(CL / "evidence"),
            "platform_dirs": DIRS, "auto": AUTO, "manual": MANUAL, "auto_env": AUTO_ENV,
            "cause": {f"{i}|{P}": v for (i, P), v in CAUSE.items()},
            "override": {f"{i}|{P}": v for (i, P), v in OVERRIDE.items()}}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    run(cfg(), ap.parse_args().dry_run)
