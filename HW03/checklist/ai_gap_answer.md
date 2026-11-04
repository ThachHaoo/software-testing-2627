# Vì sao AI bỏ sót item SV-01…SV-06 – câu trả lời của AI (T1 2/6c)

Câu trả lời của AI (Claude Opus 5.5, Claude Code) cho câu hỏi của SV, viết **sau** khi SV đã commit `sv_items.md` (`823f7b9`). Đây **không** phải cột `ly_do_AI_bo_sot` của SV (SV tự viết, không sửa).

**Căn cứ** — chỉ dùng bản v1 do AI tạo ở bước 1/6:
- `HW03/appendix/ai-outputs/T1_checklist_ai_v1.json` (65 item, đóng băng tại `39f685c`);
- `HW03/checklist/c2_inventory.md` @ `39f685c`;
- prompt của lệnh 1/6 (prompt log HW03, lượt 17:44 04/11). Prompt yêu cầu 3 nguồn: (a) điều khoản SRS, (b) checklist theo control "(text box, button, link, validation)", (c) heuristic Nielsen/Norman/Shneiderman. Prompt yêu cầu "≥ 45 item", "Không chạy SUT để chỉnh Expected theo hành vi quan sát", và không nhắc accessibility/WCAG hay hành vi riêng của thiết bị di động.

**Cách xếp nhóm:**
- (1) Đã nghĩ tới nhưng không đưa vào: chỉ khi v1 hoặc inventory có nhắc tới khía cạnh đó.
- (2) Không nghĩ tới: không có bằng chứng trong v1; ghi "không có dấu vết trong v1".
- (3) Đã có nhưng bị gỡ theo quyết định SV: đối chiếu `meta.review_log` (G1–G4, S, S2).

Mục "Nguyên nhân khả dĩ" là **nhận định của AI**, không phải dữ kiện.

## Tổng hợp

| Item | Nhóm | Bằng chứng trong v1 |
|---|---|---|
| SV-01 Focus nhìn thấy được | (2) | không có dấu vết trong v1 (chỉ có thứ tự focus) |
| SV-02 Autofill / dán | (2) | không có dấu vết trong v1 |
| SV-03 Trả focus về ô lỗi | (2) | không có dấu vết trong v1 |
| SV-04 Độ tương phản màu | (2) | không có dấu vết trong v1 |
| SV-05 Bàn phím ảo che form | (2) | không có dấu vết trong v1 (bàn phím ảo chỉ được nhắc cho phím Tab/Enter) |
| SV-06 Chống gửi trùng khi bấm nhanh | (1) | CL-53 v1 |

Nhóm (3): không item nào. Không quyết định nào trong `review_log` gỡ khía cạnh mà SV-01…SV-06 kiểm.

## Từng item

### SV-01 – Focus nhìn thấy được khi duyệt bằng bàn phím · nhóm (2)
- v1: "focus" chỉ xuất hiện ở CL-10/11/12 (thứ tự Tab: "Fail nếu focus nhảy ngược lên…", v1 dòng 184 trở đi) và CL-38 (bấm nhãn → "con trỏ nhảy vào ô", v1 dòng 640). Không item nào kiểm focus có **hiển thị** hay không; không có "outline", "focus ring". → không có dấu vết trong v1.
- Nguyên nhân khả dĩ (nhận định của AI): prompt không yêu cầu nguồn accessibility; v1 chỉ dùng WCAG cho `lang` (CL-14), `title` (CL-13), nhãn (CL-38). Inventory lập từ JSX tĩnh, không ghi lớp CSS focus của từng control, nên không có dữ kiện gợi ra khía cạnh này.

### SV-02 – Autofill và dán dữ liệu vào ô nhập · nhóm (2)
- v1, inventory: không có "autofill", "autocomplete", "paste", "dán". → không có dấu vết trong v1.
- Nguyên nhân khả dĩ (nhận định của AI): checklist theo control trong prompt và slide ("Checklist — Text Box") liệt kê trạng thái, giới hạn, lớp ký tự đầu vào; v1 bám đúng danh sách đó. Hành vi do trình duyệt cung cấp (trình quản lý mật khẩu, clipboard) không có trong mã SUT nên không xuất hiện trong inventory.

### SV-03 – Trả focus về đúng ô lỗi sau khi submit thất bại · nhóm (2)
- v1, inventory: không có "trả lại", "return focus", "offending". → không có dấu vết trong v1.
- Dữ kiện thêm: đoạn slide "Checklist — input-field validation" có câu "G O L D E N R U L E On error, return focus to the offending field and highlight it" **nằm trong phần slide AI đã đọc** ở lượt 1/6 (bản trích text, dòng 203; AI đọc dòng 56–210 và 401–460). Dù vậy v1 không có item nào cho quy tắc này, nên vẫn xếp nhóm (2) theo cách xếp ở trên. AI không có bằng chứng là mình đã cân nhắc rồi loại quy tắc này.
- Nguyên nhân khả dĩ (nhận định của AI): các item lỗi của v1 (CL-22, CL-23, CL-30, CL-32) chỉ kiểm vị trí và nội dung thông báo, bám điều khoản FR-22.4. Khi sinh item, AI ưu tiên điều khoản SRS (40/65 item v1 là SRS) và bỏ qua quy tắc này của slide.

### SV-04 – Độ tương phản màu chữ so với nền · nhóm (2)
- v1: không có "tương phản", "contrast". Inventory chỉ ghi lớp màu như một thuộc tính (`text-yellow-300` của tên người dùng trên navbar, `c2_inventory.md:14`), không có item kiểm tương phản. → không có dấu vết trong v1.
- Nguyên nhân khả dĩ (nhận định của AI): prompt không nêu accessibility. Màu trong v1 chỉ được dùng cho quy tắc màu nút của FR-21.2 (CL-04, CL-05). Ngoài ra AI không chạy SUT ở bước 1/6 (prompt cấm chỉnh Expected theo quan sát), nên không có màu render thực tế để gợi ý.

### SV-05 – Bố cục form khi bàn phím ảo hiện trên di động · nhóm (2)
- v1 có nhắc bàn phím ảo ở hai chỗ: NA1 (v1 dòng 23: "P3 dùng bàn phím ảo cảm ứng, không có phím Tab") và CL-36 (v1 dòng 610: "P3: phím Go/Enter của bàn phím ảo"). Cả hai chỉ nói về phím, không nói việc bàn phím ảo che input/nút. → không có dấu vết trong v1 cho khía cạnh SV-05 kiểm.
- Nguyên nhân khả dĩ (nhận định của AI): P3 chỉ được xem như một trình duyệt nữa của cùng checklist. Thứ v1 xét riêng cho P3 là cái *không áp dụng* được (NA1), không phải cái *chỉ có* trên di động. Khía cạnh di động duy nhất trong v1 là bố cục ở màn hẹp (CL-15), không gắn với bàn phím ảo.

### SV-06 – Chống gửi trùng khi bấm liên tiếp · nhóm (1)
- v1 có CL-53 "Có chỉ báo đang xử lý và chống gửi trùng" (v1 dòng 885–888): "DevTools Network throttling 'Slow 3G': bấm Đăng nhập → … bấm thêm 2 lần chỉ phát sinh 1 request /api/login". Như vậy AI đã nghĩ tới chống gửi trùng, nhưng chỉ đưa vào cho **một form** (Đăng nhập) và **một điều kiện** (mạng chậm). Không đưa vào cho 'Đặt lại mật khẩu', 'Cập nhật', và không kiểm bấm nhanh khi mạng bình thường.
- Nguyên nhân khả dĩ (nhận định của AI): CL-53 được viết từ heuristic phản hồi (Norman Feedback, Shneiderman #3), lấy "đang chờ" làm điểm chính, nên điều kiện thử chọn là mạng chậm. Quy tắc 4 (mỗi thuộc tính chỉ khẳng định ở một item) có thể đã khiến AI không lặp kiểm tra này cho các form khác. Slide "Double-submit on double-click" (bản trích text, dòng 53) **nằm ngoài** đoạn slide AI đã đọc ở lượt 1/6 (dòng 56–210 và 401–460), nên không có trong ngữ cảnh khi sinh v1.

## Nhận xét chung (nhận định của AI)

- 5/6 item thuộc nhóm (2). Điểm chung là khía cạnh **chỉ quan sát được khi chạy trên trình duyệt/thiết bị thật** (hiển thị focus, autofill, bàn phím ảo, tương phản) hoặc **nằm trong slide nhưng ngoài 3 nguồn prompt nêu cụ thể** (Golden Rule).
- v1 bám khá sát chữ của prompt: 3 nguồn, đúng nhóm control được liệt kê, không chạy SUT. Phần prompt không nhắc (accessibility, hành vi riêng của di động) hầu như vắng trong v1.
