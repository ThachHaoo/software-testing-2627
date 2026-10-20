# D_FR20 – AI trả lời "vì sao bản AI không có case này" (bước 5)

Đây là câu trả lời của AI (Claude Opus 5.5, Claude Code) sau khi SV đã tự thêm case (commit `f66b32f`, `HW02/D_FR20/sv_cases.md`). Nó không phải phần phân tích gap của report; phần đó do SV viết.

**Bản đối chiếu (đóng băng):**
- Bước 1: `HW02/appendix/ai-outputs/D_FR20_step1_20261020-222828.json`.
- Bước 2: `D_FR20_step2_20261020-224243.json`, `D_FR20_step2_20261020-224621.json` (2/7b).
- Bước 3: `D_FR20_step3_20261020-224808.json`, `D_FR20_step3_20261020-225134.json` (3/7b).
- Bước 4: `D_FR20_step4_20261020-225208.json` (bản cuối, 27 TC).

**Cách xếp nhóm:**
- **Nhóm 1 – Đã nghĩ tới nhưng không đưa vào:** chỉ khi output AI có dẫn chứng là chính ý hoặc giá trị đó đã được xét.
- **Nhóm 2 – Không nghĩ tới:** không có dẫn chứng. AI vẫn ghi lớp EC gần nhất để thấy case SV khác ở chỗ nào; điều đó không có nghĩa AI đã nghĩ tới case.
- **Nhóm 3 – Đã có nhưng bị gỡ theo quyết định SV:** output AI có đề xuất phương án chứa ý này, SV chọn phương án khác.

**Liên quan P1 = b:** AI không đọc case SV của A (`sv_cases.md`, `ai_gap_answer.md`, `sv_questions.md`) ở bước 1–4, nên AI không biết A có case tương tự hay không. Những gì AI đã thấy từ bước 5 của A qua `A_FR01/testcases.json` được liệt kê ở `step1_notes.md` mục 6; chỗ nào liên quan được ghi ở từng case dưới đây.

## Nhóm 1 – Đã nghĩ tới nhưng không đưa vào

| Case SV | Dẫn chứng trong output AI | Vì sao không có trong bản bước 3–4 |
|---|---|---|
| TC-FR20-206 (Họ Tên 10.000 ký tự, dán) | Bước 1: D3 "không có cận trên độ dài" cho Họ Tên. Bước 4: mô tả TS-BVA "Họ Tên không làm BVA ở tầng Mobile theo D1 = a"; TC-FR20-64 (LARGE của Mật khẩu, 64 ký tự) ghi "có thể dán chuỗi từ bộ nhớ tạm". | AI đã xét "Họ Tên không có cận trên" và đường nhập bằng dán, nhưng giới hạn BVA vào Mật khẩu theo phạm vi gọn mà AI đề xuất ở D1 (a). Ngay cả phương án D1 (b) cũng chỉ chép BVA của A, mà A không có điểm giá trị lớn cho Họ Tên (A1). Độ dài cực lớn và tác động tới hiệu năng của app (đơ UI) không được xét. |

## Nhóm 2 – Không nghĩ tới

| Case SV | Lớp gần nhất mà bản AI có | Ghi chú nguyên nhân |
|---|---|---|
| TC-FR20-200 (dán `<script>alert(1)</script>` vào Họ Tên) | EC1 Họ Tên không rỗng, đại diện 'Nguyễn Văn Ánh' (TC-01). D12 có xét "dán" nhưng gộp với gõ. | SEC-04 không có trong requirements hay giả định nào của D; `meta.references` chỉ nêu SEC-01. Liên quan P1 = b: ở bước 1 AI có thấy dòng scope của A "TS-SV có kiểm thăm dò SEC-04, SEC-05, SEC-06*", nhưng không đưa SEC-04 vào D. |
| TC-FR20-201 (Emoji 🐻 trong Họ Tên) | EC1; note EC1 (bước 2): gộp A EC1 + EC2, "A tách vì mã hoá/lưu trữ phía server". | AI có nhắc tới khác biệt mã hoá (ASCII và tiếng Việt có dấu), nhưng gộp lại theo D1 = a. Ký tự ngoài BMP (emoji 4 byte) không xuất hiện trong output nào. |
| TC-FR20-202 (Mật khẩu có `\n`, dán từ Ghi chú) | EC20 "có ký tự trong tập và thêm ký tự đặc biệt ngoài tập" (TC-02, `'#'`); D7. | Ký tự điều khiển/xuống dòng không được xét là một loại ký tự của Mật khẩu. "Dán" chỉ được xét ở D12 như một cách nhập cùng chuỗi. |
| TC-FR20-203 (chạm 'Đăng Ký' 10 lần) | EC31 tạo đúng 1 tài khoản (TC-01). | Mô hình miền xét từng lần thao tác; quy trình TS-DOM ghi "bấm nút 'Đăng Ký' đúng một lần". Không có biến nào về số lần hay tốc độ bấm. |
| TC-FR20-205 (chữ số full-width trong Mật khẩu) | EC17/EC18 có/không có chữ số 0–9; D8 chỉ nói về chữ hoa/thường có dấu. | AI có xét ký tự ngoài ASCII cho chữ cái (D8, EC13, EC16), nhưng không mở rộng sang chữ số Unicode. |
| TC-FR20-207 (bàn phím che ô Mật khẩu / nút 'Đăng Ký') | TS-GUI theo D13: FR-22.1–22.4 (TC-90…93). | Bàn phím ảo chỉ được xét ở loại bàn phím (TC-91, FR-22.2) và ở D12 (tự sửa/tự viết hoa). Việc bàn phím chiếm chỗ trên màn hình không xuất hiện trong output nào. |
| TC-FR20-208 (nút 'Mắt' hiện/ẩn mật khẩu) | TC-FR20-92 kiểm ô Mật khẩu che ký tự (FR-22.3, D13). | AI chỉ hiểu FR-22.3 là "che ký tự" và kiểm một trạng thái. Chức năng chuyển hiện/ẩn không được xét. |

## Nhóm 3 – Đã có nhưng bị gỡ theo quyết định SV

| Case SV | Dẫn chứng trong output AI | Quyết định SV |
|---|---|---|
| TC-FR20-204 (bàn phím tự sửa chèn khoảng trắng vào Email) | Bước 1: căn cứ D12 nêu bàn phím ảo "tự viết hoa / tự sửa / gợi ý"; D12 (b) "cách nhập (gõ / dán / chọn gợi ý) là biến vào có lớp riêng → thêm case". Bước 2: EC5 gộp các lớp sai định dạng của A, trong đó có "khoảng trắng bên trong" (A EC15), tham chiếu TC-FR01-40 (API). Bước 3: quy trình TS-DOM bước 4 "Bàn phím tự viết hoa/tự sửa/chèn gợi ý làm đổi chuỗi → xoá và gõ lại cho đúng". | D12 = a (giá trị case = chuỗi trong ô; cách nhập không là biến) và D1 = a (lớp con do server xử lý lấy 1 đại diện). Vì vậy bản AI cố ý loại tác động của bàn phím khỏi case thay vì kiểm nó. |

## Đếm

- Nhóm 1: 1 (TC-206) · Nhóm 2: 7 (TC-200, 201, 202, 203, 205, 207, 208) · Nhóm 3: 1 (TC-204).

## Rà nhất quán case SV (chỉ liệt kê, không sửa)

Cập nhật ở 5/7f theo `sv_cases.md` commit `e067035`. SV đã bỏ TC-FR20-202 (5/7c) và TC-FR20-207, 208 (5/7e); giữ khoảng trống số. SV thêm D16.

- TC-FR20-200: không thấy lỗi nhất quán.
- TC-FR20-201: không thấy lỗi nhất quán.
- TC-FR20-203: hết lỗi — câu quy trình TS-SV (do AI viết) đã sửa ở 5/7f thành "đúng số lần ghi trong case (mặc định 1 lần)"; Lý do chọn input của SV ghi 10 lần.
- TC-FR20-204: không thấy lỗi nhất quán.
- TC-FR20-205: tiêu đề "chỉ chứa các chữ số Full-width `Abcd１２３４５６７８`" khác giá trị nhập `Abcd１２３４５６!` (tiêu đề có `７８`, giá trị có `!`), và chuỗi trong tiêu đề có chữ cái nên không "chỉ chứa chữ số". D16 dẫn căn cứ "D8 (chữ số 0-9)", nhưng D8 chỉ nói về chữ hoa/thường (A–Z / a–z), không nói chữ số.
- TC-FR20-206: không thấy lỗi nhất quán.