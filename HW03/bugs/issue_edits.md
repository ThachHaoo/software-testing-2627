# Sửa issue sau khi tạo (log)

## 11/11/2026 – #266 (BUG-72)

- Lý do: dòng dữ kiện "Actual nguyên văn CL-32 P3 (auto)" (mục "Dữ kiện (AI chép)") bị SV lỡ xoá một đoạn ở commit `496ad20`; khôi phục đúng `notes_nt.P3` của CL-32 trong `checklist/checklist.json` (bỏ tiền tố `[auto – …]` như cách sinh khung bug). Chỉ đổi dòng này, phần còn lại của body (gồm ảnh SV đã kéo vào) giữ nguyên.
- Trước:
  - Actual nguyên văn CL-32 P3 (auto): `Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"`
- Sau:
  - Actual nguyên văn CL-32 P3 (auto): `Lỗi: Error: 912345678 được lưu · Lỗi: Error: thông báo không nêu: 0, 10, 11 · thông báo: "Cập nhật thành công!"; sau F5: "912345678"`
- Đã làm: sửa `bugs/BUG-72.md`; `gh issue edit 266 --body-file` (body hiện tại trên GitHub, thay đúng dòng trên); comment đính chính https://github.com/tkob-team/eshop-sut/issues/266#issuecomment-6783987589 ("Đính chính: khôi phục dòng dữ kiện CL-32 P3 chép từ checklist.json").
