# RUN – chạy checklist `<scope>`

Bước 3 của skill `gui-checklist-testing`. AI điền khung, SV sửa cho khớp cách chạy thật **trước** khi chạy; sửa sau đó thì freeze lại, Expected không đổi.

## 1. Chuẩn bị (mỗi nền tảng)

- Khởi động SUT: `<lệnh backend>`, `<lệnh web>`; nền tảng di động: `<adb reverse …>`.
- Restart backend trước lượt chính thức (CSDL seed lại). Tài khoản: `<…>`.
- Ghi phiên bản: trình duyệt `<…>`, OS `<…>`, thiết bị `<…>`, độ phân giải `<…>`.
- Overlay ảnh theo đề: `<MSSV · họ tên · email>`; ảnh thấy tên trình duyệt + URL.

## 2. Thứ tự nhóm item

| Nhóm | Tiền điều kiện chung | Item | Ghi chú |
|---|---|---|---|
| G1 | `<…>` | CL-xx, … | |

## 3. Ảnh

| Loại | Khi nào | Tên file |
|---|---|---|
| Bắt buộc | item Failed | `checklist/evidence/<Px>_<tên>/CL-xx_failed.png` |
| Không chụp | Passed, N/A | — |

Trần số ảnh mỗi nền tảng: `<n>` (giới hạn 20 MB/file khi nộp).

## 4. Ghi kết quả

File lượt `checklist/runs/<Px>_<YYYYMMDD-HHMM>.csv`, header `id,status,notes,evidence`. `status` ∈ Passed / Failed / N/A / Blocked; Failed ghi Actual nguyên văn trong `notes`; Blocked ghi item gốc. Gộp:

```powershell
python .claude/skills/gui-checklist-testing/scripts/merge_platform.py <dir>/checklist.json <dir>/runs/<file>.csv --platform <Px> --dry-run
python .claude/skills/gui-checklist-testing/scripts/merge_platform.py <dir>/checklist.json <dir>/runs/<file>.csv --platform <Px>
```

## 5. Nhật ký lượt chạy

| Lượt | Nền tảng | Bắt đầu – kết thúc | Chính thức? | Ghi chú |
|---|---|---|---|---|
