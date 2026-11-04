"""Sinh HW03/checklist/RUN.md (phần chạy tay) + runs/<P>_manual_TEMPLATE.md từ checklist.json.

    python HW03/tests/gen_run.py

Thứ tự theo màn hình (không theo số item). "Cần nhìn" = Expected nguyên văn (item manual, P3) hoặc phần chạy tay
của item mixed (che_do_ghi_chu). Chạy lại khi checklist.json đổi.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
doc = json.loads((root / "checklist" / "checklist.json").read_text(encoding="utf-8"))
items = doc["items"]
SCREENS = [("M1", "Đăng nhập"), ("M2", "Quên mật khẩu (B1, B2)"), ("M3", "Hồ sơ"), ("M4", "Lịch sử đơn"), ("M5", "Navbar"), ("M6", "Chung – tất cả màn C2")]
LAST = ["CL-52", "CL-64"]          # khoá tài khoản / tắt backend → cuối lượt
FIRST = ["CL-62"]                  # cần tài khoản chưa có đơn → đầu lượt, trước khi dựng đơn
OVERLAY = "23120255 · Lê Tấn Hiệp · 23120255@student.hcmus.edu.vn"


def screen(it):
    m = it["man_hinh"]
    if "Lịch sử đơn" in m:
        return "M4"
    if m.startswith("Tất cả"):
        return "M6"
    if m.startswith("Navbar"):
        return "M5"
    if m.startswith("Hồ sơ"):
        return "M3"
    if m.startswith("Quên mật khẩu"):
        return "M2"
    return "M1"


def look(it, P):
    if it.get("che_do") == "manual" or (it.get("auto_nen_tang") and P not in it["auto_nen_tang"]):
        return it["expected"]
    return f"Phần chạy tay: {it.get('che_do_ghi_chu', '')}. Phần tự động: xem `runs/{P}_auto_*.json`."


def rows(P):
    sel = []
    for it in items:
        if P not in it.get("nen_tang", []):
            continue
        if it.get("che_do") in ("manual", "mixed") or (it.get("auto_nen_tang") and P not in it["auto_nen_tang"]):
            sel.append(it)
    return sel


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def table(P, sel):
    out = []
    first = [i for i in sel if i["id"] in FIRST]
    last = [i for i in sel if i["id"] in LAST]
    mid = [i for i in sel if i["id"] not in FIRST + LAST]
    n = P[1]
    def block(title, its):
        if not its:
            return
        out.append(f"#### {title}\n")
        out.append("| ☐ | Item | Màn hình | Mục kiểm tra | Tiền điều kiện | Cần nhìn (ngưỡng Pass/Fail) |")
        out.append("|---|---|---|---|---|---|")
        for it in its:
            out.append(f"| ☐ | {it['id']} | {cell(it['man_hinh'])} | {cell(it['muc_kiem_tra'])} | {cell(it.get('tien_dieu_kien', ''))} | {cell(look(it, P))} |")
        out.append("")
    block("Bước A – ngay sau khi restart backend (tài khoản chưa có đơn)", first)
    out.append(f"**Bước B – dựng đơn:** `python HW03/tests/seed_orders.py` → ghi lại bảng mã đơn ↔ trạng thái vào file kết quả.\n")
    for code, name in SCREENS:
        its = [i for i in mid if screen(i) == code]
        if its:
            block(f"{code} – {name} · ảnh tổng quan bắt buộc: `P{n}_{code}_1.png`", its)
    block("Cuối lượt (khoá tài khoản / tắt backend – làm sau cùng)", last)
    return out


md = [
    "# RUN – chạy tay checklist C2 (T1 bước 3, sinh bằng `HW03/tests/gen_run.py`)",
    "",
    f"Nguồn: `checklist.json` ({doc['meta'].get('version', '')}); {len(items)} item. Phần tự động (Playwright, P1 Chrome + P2 Firefox của Playwright + P3 Chrome Android thật qua `_android`) chạy trước, ghi `auto_status`; **verdict chính thức = lượt chạy tay trên trình duyệt thật** (report_plan E2). Expected không đổi; procedure sai → sửa RUN.md trước khi chạy.",
    "",
    "## 1. Mỗi nền tảng = 1 lượt",
    "",
    "1. Restart backend: dừng `node server.js` rồi `cd ..\\eshop-sut\\backend; node server.js` (CSDL seed lại). Web: `cd ..\\eshop-sut\\frontend-web; npx vite --host 127.0.0.1 --port 5173`.",
    "2. Ghi phiên bản trình duyệt + OS (+ máy) vào đầu file kết quả.",
    "3. Làm Bước A → Bước B → M1…M6 → Cuối lượt, theo bảng của nền tảng đó (mục 4).",
    "4. Item đổi mật khẩu (CL-27, CL-29, CL-48, SV-06): xong thì `python HW03/tests/seed_orders.py --restore-password`.",
    "5. Item đổi hồ sơ: xong thì trả Họ Tên `Test User`, xoá SĐT/địa chỉ.",
    "6. **Cảnh báo (gray-box, `backend/server.js:54–57`):** mỗi lần sai mật khẩu bộ đếm tăng 2, ≥ 3 là khoá **180 giây** → sau một lần đăng nhập sai, đăng nhập đúng ngay để đưa bộ đếm về 0. CL-52 làm cuối lượt.",
    "",
    "**P3 (Chrome Android, POCO F5):**",
    "",
    "```powershell",
    "D:\\Tools\\platform-tools\\adb.exe devices          # phải là \"<serial>  device\"",
    "D:\\Tools\\platform-tools\\adb.exe reverse tcp:5173 tcp:5173",
    "D:\\Tools\\platform-tools\\adb.exe reverse tcp:3000 tcp:3000",
    "D:\\Tools\\platform-tools\\adb.exe reverse --list",
    "```",
    "",
    "Lượt auto P3: `npx playwright test --project=P3` trong `HW03/tests` (Playwright `_android`; cần adb server đang chạy, điện thoại mở khoá, flag Chrome *Enable command line on non-rooted devices* bật). Playwright sẽ đóng rồi mở lại Chrome trên máy, xoá cookie/storage của `localhost:5173` và `localhost:3000` trước mỗi test.",
    "",
    "Chạy tay P3: mở `http://localhost:5173` trên Chrome điện thoại. Item cần DOM/đo (h1, type, toạ độ, màu…): PC mở `chrome://inspect` → *inspect* tab của điện thoại → Console, dán `HW03/checklist/dom_probe.js`, chép JSON vào file kết quả. Rút cáp / restart adb → chạy lại 2 lệnh `reverse`.",
    "",
    "## 2. Ảnh",
    "",
    f"- Overlay trên MỌI ảnh: `{OVERLAY}`. PC: cửa sổ Sticky Notes ghi dòng này, chụp **toàn màn hình** (thấy tên trình duyệt + URL). Điện thoại: chụp rồi thêm chữ bằng trình sửa ảnh của máy ngay sau khi chụp (thấy thanh URL).",
    "- Bắt buộc: (a) mỗi item **Failed**: `P<n>_<id>_<k>.png` (vd `P1_CL-22_1.png`); (b) Task 3: **1 ảnh tổng quan mỗi màn / nền tảng**: `P<n>_M<k>_1.png` (M1…M5).",
    "- Không chụp: item Passed, N/A.",
    "- Thư mục: `HW03/checklist/evidence/P1_chrome/`, `P2_firefox/`, `P3_android/`. Mỗi file ≤ 20 MB.",
    "",
    "## 3. Ghi kết quả",
    "",
    "Ghi vào bản sao của `runs/<P>_manual_TEMPLATE.md` → `runs/<P>_manual_<YYYYMMDD-HHMM>.md`: mỗi item một dòng `status` (Passed / Failed / N/A / Blocked) + notes (Failed: Actual nguyên văn; Blocked: item gốc) + tên ảnh. AI chép sang CSV và gộp bằng `merge_platform.py`.",
    "",
    "## 4. Bảng theo nền tảng",
    "",
]
for P, name in doc["meta"]["platforms"].items():
    sel = rows(P)
    md.append(f"### {P} – {name} ({len(sel)} item chạy tay)\n")
    md += table(P, sel)
md += ["## 5. Nhật ký lượt", "", "| Lượt | Nền tảng | Bắt đầu – kết thúc | Restart backend | Chính thức? | Ghi chú |", "|---|---|---|---|---|---|", ""]
(root / "checklist" / "RUN.md").write_text("\n".join(md) + "\n", encoding="utf-8")

runs = root / "checklist" / "runs"
runs.mkdir(exist_ok=True)
for P, name in doc["meta"]["platforms"].items():
    sel = rows(P)
    t = [f"# {P} – kết quả chạy tay ({name})", "", "- Trình duyệt / phiên bản:", "- OS / thiết bị:", "- Bắt đầu – kết thúc:", "- Restart backend lúc:",
         "- Mã đơn (seed_orders.py):", "", "| Item | status | notes | ảnh |", "|---|---|---|---|"]
    t += [f"| {i['id']} | | | |" for i in sel]
    t += ["", "## Ảnh tổng quan Task 3", "", "| Màn | ảnh |", "|---|---|"] + [f"| {c} | |" for c, _ in SCREENS[:5]]
    (runs / f"{P}_manual_TEMPLATE.md").write_text("\n".join(t) + "\n", encoding="utf-8")
print("RUN.md:", {P: len(rows(P)) for P in doc["meta"]["platforms"]})
