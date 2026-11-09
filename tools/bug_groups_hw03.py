"""Gom item Failed MỚI của HW03 thành nhóm dữ kiện G-xx + sinh khung bugs/BUG-<n>.md CHỈ chứa dữ kiện chép lại.

    python tools/bug_groups_hw03.py [--skeleton]       # --skeleton: tạo khung BUG chưa có (không ghi đè file đã có)

- Nhóm (GROUPS) do AI đề xuất theo dữ kiện quan sát giống nhau (cùng phần tử / cùng hành vi, khác màn/nền tảng);
  SV xác nhận/tách/gộp rồi mới viết bug. Item MỘT PHẦN (failed_list) chỉ lấy phần màn chưa có issue.
- Khung BUG: item, nền tảng, môi trường, nguồn bước (chép nguyên văn từ checklist/test, không phải Steps), Expected chép,
  Actual chép notes, ảnh. Tiêu đề / Mô tả / Steps / Severity / Priority / Nhận định để trống – SV viết 🔒.
"""
import argparse, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from failed_list_hw03 import DUP  # noqa: E402

for _s in (sys.stdout,):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

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
# (mã nhóm, dữ kiện chung quan sát được, [item]) – AI đề xuất, SV xác nhận
GROUPS = [
    ("G-01", "Thứ tự Tab không theo vị trí hiển thị (focus bắt đầu ở form, navbar bị đi sau / bỏ qua)", ["CL-10", "CL-12"]),
    ("G-02", "Thông tin mức tài liệu giống nhau ở mọi trang: title \"frontend-web\", <html lang=\"en\">", ["CL-13", "CL-14"]),
    ("G-03", "Trang không có thẻ <h1>", ["CL-02"]),
    ("G-04", "Ô Email bước 1 Quên mật khẩu: type=\"text\", email sai định dạng vẫn gửi request (phần /login trùng #4)", ["CL-17", "CL-66"]),
    ("G-05", "Nhãn trường bắt buộc thiếu '*' ở Quên mật khẩu B1/B2 và Hồ sơ (phần /login trùng #7)", ["CL-20", "CL-21"]),
    ("G-06", "Lỗi validate chỉ hiện ở hộp thoại trình duyệt (Quên MK B2, Hồ sơ)", ["CL-23"]),
    ("G-07", "Bấm nhãn không focus ô nhập (Đăng nhập, Hồ sơ)", ["CL-38"]),
    ("G-08", "Quên mật khẩu: không có chỉ báo bước", ["CL-24"]),
    ("G-09", "Quên mật khẩu B1: không có 'Quay lại đăng nhập'", ["CL-25"]),
    ("G-10", "Quên mật khẩu B2: không có ô Xác nhận mật khẩu mới", ["CL-26"]),
    ("G-11", "Mã OTP hiển thị 4 chữ số", ["CL-28"]),
    ("G-12", "Quên mật khẩu B2: mật khẩu 'Abcdef1!' bị báo yếu", ["CL-29"]),
    ("G-13", "Kiểu nút ở Quên mật khẩu B2: 'Đặt lại mật khẩu' màu xanh lá; nút chính và nút phụ giống nhau", ["CL-04", "CL-06"]),
    ("G-14", "Hồ sơ: SĐT '912345678' được lưu, thông báo không nêu quy tắc (phần lưu liên quan #97/#113)", ["CL-32"]),
    ("G-15", "Hồ sơ: sau Cập nhật + F5, trường quay về giá trị cũ", ["CL-37"]),
    ("G-16", "Navbar: link hồ sơ không đổi kiểu theo trang hiện tại", ["CL-40"]),
    ("G-17", "Navbar: nút đăng xuất nhãn \"Thoát\"", ["CL-42"]),
    ("G-18", "Navbar: đổi Họ Tên, navbar giữ tên cũ tới khi tải lại", ["CL-56"]),
    ("G-19", "/profile khi chưa đăng nhập: không chuyển, không có link tới Đăng nhập", ["CL-49"]),
    ("G-20", "URL không tồn tại: vùng nội dung trống, không có link về trang chủ", ["CL-50"]),
    ("G-21", "Nút submit không khoá / không có chỉ báo khi bấm nhiều lần (Đăng nhập, Quên MK B1/B2, Hồ sơ)", ["CL-53", "SV-06"]),
    ("G-22", "Lịch sử đơn: không có trạng thái đang tải", ["CL-63"]),
    ("G-23", "Lịch sử đơn: định dạng Tổng tiền và Ngày đặt khác nhau giữa các nền tảng", ["CL-08", "CL-09"]),
    ("G-24", "Lịch sử đơn: nút 'Hủy đơn' dùng được ở đơn đang giao", ["CL-59"]),
    ("G-25", "Lịch sử đơn: bấm 'Hủy đơn' huỷ ngay, không có hộp xác nhận", ["CL-60"]),
    ("G-26", "Lịch sử đơn trống: không có icon/hình minh hoạ", ["CL-62"]),
    ("G-27", "Autofill của trình duyệt không điền được (dán được)", ["SV-02"]),
    ("G-28", "Submit thất bại: focus không về ô lỗi", ["SV-03"]),
    ("G-29", "Độ tương phản chữ/nhãn dưới 4.5:1 ở Đăng nhập, Hồ sơ", ["SV-04"]),
    ("G-30", "Link 'Quên mật khẩu?', 'Đăng ký ngay' nhỏ hơn 24×24 px", ["SV-05"]),
]


def strip(n):
    return re.sub(r"^\[auto – [^\]]*\] ", "", n or "")


def spec_line(iid):
    for k, l in enumerate((ROOT / "tests" / "C2.spec.ts").read_text(encoding="utf-8").splitlines(), 1):
        if l.startswith(f"test('{iid} "):
            return f"`HW03/tests/C2.spec.ts:{k}`"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skeleton", action="store_true")
    a = ap.parse_args()
    doc = json.loads((ROOT / "checklist" / "checklist.json").read_text(encoding="utf-8"))
    items = {i["id"]: i for i in doc["items"]}
    plats = list(doc["meta"]["platforms"])

    def failed(it):
        return [P for P in plats if it.get("ket_qua", {}).get(P) == "Failed" and it.get("lap_bug", {}).get(P) is not False]

    new = {iid for iid, it in items.items() if failed(it) and DUP.get(iid, ("MỚI",))[0] != "TRÙNG"}
    grouped = [x for _, _, its in GROUPS for x in its]
    dupl = {x for x in grouped if grouped.count(x) > 1}
    if set(grouped) != new or dupl:
        sys.exit(f"Nhóm chưa khớp danh sách MỚI: thiếu {sorted(new - set(grouped))}, thừa {sorted(set(grouped) - new)}, lặp {sorted(dupl)}")

    md = ["# Nhóm dữ kiện bug – T1 checklist C2 (đề xuất, SV xác nhận 🔒)", "",
          f"Sinh bằng `tools/bug_groups_hw03.py` từ `checklist.json` + `failed_list.md`. {len(new)} item Failed MỚI / trùng một phần → **{len(GROUPS)} nhóm**. "
          "Gom theo dữ kiện quan sát giống nhau (cùng phần tử hoặc cùng hành vi, khác màn/nền tảng); AI không kết luận nguyên nhân. "
          "SV tách/gộp nhóm, rồi viết BUG từ khung tương ứng. Expected/Actual chép nguyên văn từ checklist (Actual = notes chạy tay hoặc số đo auto).", "",
          "| Nhóm | Khung | Dữ kiện chung | Item | Nền tảng Failed | Trùng / liên quan |", "|---|---|---|---|---|---|"]
    detail, made = [], []
    for k, (g, fact, its) in enumerate(GROUPS):
        bug = f"BUG-{FIRST_BUG + k}"
        ps = sorted({P for x in its for P in failed(items[x])})
        rel = "; ".join(f"{x}: {DUP[x][0].lower()} " + ", ".join(f"#{n}" for n in DUP[x][1]) for x in its if x in DUP)
        md.append(f"| {g} | `{bug}.md` | {fact} | {', '.join(its)} | {', '.join(ps)} | {rel or '–'} |")
        detail.append(f"## {g} → `{bug}.md` – {fact}\n")
        body = []
        for x in its:
            it = items[x]
            f = failed(it)
            detail.append(f"### {x} – {it['muc_kiem_tra']} ({it['man_hinh']})\n")
            detail.append(f"- Căn cứ: {it.get('can_cu', '')}")
            detail.append(f"- Expected (chép): {it['expected']}")
            for P in f:
                ev = ", ".join(f"`{e}`" for e in it.get("evidence", {}).get(P, [])) or "–"
                detail.append(f"- Actual {P} ({it.get('nguon_kq', {}).get(P)}): {strip(it['notes_nt'].get(P, ''))} · ảnh: {ev}")
            detail.append("")
            body += [f"### {x} – {it['muc_kiem_tra']}", "", f"- Màn hình: {it['man_hinh']}", f"- Căn cứ: {it.get('can_cu', '')}",
                     f"- Nền tảng Failed: {', '.join(f)}" + (f" · trùng một phần/liên quan: {', '.join('#' + str(n) for n in DUP[x][1])} ({DUP[x][2]})" if x in DUP else ""),
                     "", "**Môi trường**", ""] + [f"- {ENV[(P, it.get('nguon_kq', {}).get(P))]}" for P in f] + [f"- SUT: {SUT}", "",
                     "**Nguồn bước tái hiện (chép nguyên văn – SV viết lại thành Steps)**", "",
                     f"- Tiền điều kiện (checklist): {it.get('tien_dieu_kien') or '–'}",
                     f"- Cách kiểm (checklist): {it.get('che_do_ghi_chu') or '–'}",
                     f"- Test tự động: {spec_line(x) or '– (item chạy tay, xem `checklist/RUN.md`)'}", "",
                     "**Expected (chép từ checklist)**", "", f"> {it['expected']}", "", "**Actual (chép notes / số đo)**", ""]
            for P in f:
                body.append(f"- {P} ({it.get('nguon_kq', {}).get(P)}): {strip(it['notes_nt'].get(P, ''))}")
            body += ["", "**Ảnh**", ""] + [f"- {P}: " + (", ".join(f"`../checklist/{e}`" for e in it.get("evidence", {}).get(P, [])) or "–") for P in f] + [""]
        if a.skeleton:
            p = ROOT / "bugs" / f"{bug}.md"
            if p.exists():
                print(f"giữ {p.name} (đã có)")
                continue
            head = [f"# {bug}", "", f"- **ID:** {bug}", f"- **Nhóm dữ kiện:** {g} ({', '.join(its)})",
                    "- **Tiêu đề:** 🔒 SV viết", "- **Mô tả:** 🔒 SV viết", "- **Steps to reproduce:** 🔒 SV viết (từ nguồn bước bên dưới)",
                    "- **Severity:** 🔒 SV chọn", "- **Priority:** 🔒 SV chọn", "- **Nhận định:** 🔒 SV viết", "- **GitHub Issue:** (sau khi tạo)", "",
                    "---", "", "## Dữ kiện (AI chép từ `checklist.json`, không sửa)", ""]
            p.write_text("\n".join(head + body), encoding="utf-8")
            made.append(p.name)
    (ROOT / "bugs" / "bug_groups.md").write_text("\n".join(md + [""] + detail), encoding="utf-8")
    print(f"{len(new)} item MỚI → {len(GROUPS)} nhóm; khung mới: {len(made)} ({made[0] if made else '–'} … {made[-1] if made else '–'})")


if __name__ == "__main__":
    main()
