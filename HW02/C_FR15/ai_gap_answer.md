# C_FR15 – AI trả lời "vì sao bản AI không có case này" (bước 5)

Đây là câu trả lời của AI (Claude Opus 5.5, Claude Code) sau khi SV đã tự thêm case (commit `c22e3da`, `HW02/C_FR15/sv_cases.md`). Nó không phải phần phân tích gap của report; phần đó do SV viết.

**Bản đối chiếu:**
- Bước 1: `HW02/appendix/ai-outputs/C_FR15_step1_20261020-162618.json`.
- Bước 2: `C_FR15_step2_20261020-163945.json`, `C_FR15_step2_20261020-164315.json`.
- Bước 3: `C_FR15_step3_20261020-165215.json`, `C_FR15_step3_20261020-165700.json` (bản tách suite).
- Bước 4: `C_FR15_step4_20261020-165850.json` (bản cuối, 111 TC).

**Cách xếp nhóm:**
- **Nhóm 1 – Đã nghĩ tới nhưng không đưa vào:** chỉ khi output AI có dẫn chứng là chính ý hoặc giá trị đó đã được xét.
- **Nhóm 2 – Không nghĩ tới:** không có dẫn chứng. AI vẫn ghi lớp EC gần nhất trong bản AI để thấy case SV khác ở chỗ nào; điều đó không có nghĩa AI đã nghĩ tới case.
- **Nhóm 3 – Đã có nhưng bị gỡ theo quyết định SV:** không có case nào thuộc nhóm này. Các thứ bị gỡ theo quyết định SV (V15 + FR-12.1 theo C5 = a) không trùng case SV nào.

## Nhóm 1 – Đã nghĩ tới nhưng không đưa vào

| Case SV | Dẫn chứng trong output AI | Vì sao không có trong bản bước 3–4 |
|---|---|---|
| TC-FR15-200 (`<script>` vào ô Tên ở form Thêm) | Bước 1: C12 đưa SEC-04 "tên sản phẩm hiển thị an toàn" vào TS-GUI. Bước 3: TC-FR15-94 tạo sản phẩm tên `<i>SEC04 {ts}</i>` qua API rồi xem ô 'Tên SP' trong bảng. | AI đã kiểm SEC-04 cho tên nhưng ở **một** case (quy ước "thuộc tính chung khẳng định một nơi"). AI chọn thẻ `<i>` vô hại và tạo dữ liệu qua API, không qua form. Payload `<script>` và đường nhập qua form không được xét. |
| TC-FR15-204 (2 tab: Tab 1 xoá M, Tab 2 sửa M) — *SV đã bỏ ở 5/7c* | Bước 1: C10 "id không tồn tại … Chỉ tạo được ở tầng API (UI chỉ chọn được sản phẩm đang hiển thị)". Bước 2: EC42–EC44 chỉ ở API. | AI đã xét "id không tồn tại" ở UI và kết luận không tạo được, vì nó giả định bảng luôn khớp CSDL. Dữ liệu cũ trên một tab khác (stale) là cách tạo được, nhưng AI không nghĩ tới. Quy trình UI cũng giả định một tab mỗi case. |
| TC-FR15-208 (price −999999999999 qua API) | Bước 2: EC19 "[Thêm] Số ≤ 0 (vd 0; -1000)". Bước 3: TC-FR15-28 dùng -1000. | Giá âm đã được xét. Theo minimum set, mỗi lớp chỉ có một đại diện nên AI chọn -1000. Giá trị âm có độ lớn cực đại không được tách thành case riêng. |
| TC-FR15-215 (price = 2^53 + 1) — *SV đã bỏ ở 5/7d* | Bước 4: lý do của điểm LARGE (TC-FR15-71, 83, 105, 117): "1 nghìn tỷ ₫, vẫn là số nguyên biểu diễn chính xác". | AI đã nghĩ tới giới hạn biểu diễn chính xác của số và **cố ý chọn LARGE nằm dưới giới hạn đó**, để case LARGE chỉ kiểm "không có cận trên" (C2) mà không lẫn lỗi độ chính xác. Giới hạn đó không được đưa thành case riêng. |
| TC-FR15-217 (khoảng trắng đầu/cuối tên ở UI) — *SV đã bỏ ở 5/7c* | Bước 1: C4 "Điểm biên độ dài dùng chuỗi ASCII không có khoảng trắng đầu/cuối để tránh phụ thuộc cách đếm/cắt". C3 chỉ quyết chuỗi **chỉ gồm** khoảng trắng. | AI thấy việc cắt khoảng trắng là chỗ SRS im lặng. AI chủ động né nó trong chọn đại diện thay vì đề xuất một giả định cho SV chốt. |

## Nhóm 2 – Không nghĩ tới

| Case SV | Lớp gần nhất mà bản AI có | Ghi chú nguyên nhân |
|---|---|---|
| TC-FR15-201 (`1e5` vào ô Giá tiền) | EC17 số nguyên > 0, đại diện 1500000 (TC-01). | Không xét cách viết khác của cùng một giá trị số (ký hiệu số mũ mà input type=number cho gõ). |
| TC-FR15-202 (`00700000`) | EC17, đại diện 1500000. | Không xét định dạng chuỗi của số hợp lệ (số 0 đứng đầu). |
| TC-FR15-203 (bấm 'Lưu sản phẩm' 10 lần) — *SV đã bỏ ở 5/7c* | EC1/EC56 thêm đúng 1 bản ghi (TC-01). | Mô hình miền xét từng lần thao tác. Không có biến nào về số lần hay tốc độ bấm; quy trình ghi "bấm đúng một lần". |
| TC-FR15-205 (`１５０００００` full-width vào ô Giá tiền) | EC20 "UI: ô 'Giá tiền' để trống"; note EC20 (bước 2): "Chuỗi không phải số gõ vào ô type=number cho giá trị rỗng → cùng lớp". | AI gộp mọi chuỗi không phải số vào lớp trống và chọn `''`. Chữ số Unicode full-width (nhìn như số) không xuất hiện trong output nào. |
| TC-FR15-206 (Sửa SP1 rồi bấm Sửa SP2, không Hủy sửa) | EC67 các sản phẩm khác giữ nguyên (TC-03, TC-19: sửa **một** sản phẩm). | Không có biến về trạng thái form trước thao tác (đang sửa sản phẩm khác). Nút 'Hủy sửa' bị C13 xếp "SRS im lặng". |
| TC-FR15-207 (SQL injection trong name) | EC5 tên hợp lệ 1–255. Bước 1 có tham chiếu README dòng 274–284 (cả bảng SEC) nhưng requirements chỉ lấy SEC-02, 03, 04. | SEC-05 (Parameterized Query) không có trong bất kỳ output nào. AI chỉ chọn các SEC liên quan tới quyền và hiển thị. |
| TC-FR15-209 (price = `Infinity` thô) | EC22/EC23 price sai kiểu (`"abc"`, `"100000"`), EC69. | Mọi case API của AI gửi JSON hợp lệ. Không xét body không phải JSON. |
| TC-FR15-210 (category_id là mảng) — *SV đã bỏ ở 5/7d* | EC34 "category_id là chuỗi chữ", đại diện `"abc"` (TC-34). | Lớp sai kiểu có, nhưng chỉ chọn đại diện chuỗi. Không có dẫn chứng AI đã xét kiểu mảng/object. |
| TC-FR15-211 (Content-Type: text/plain) | EC69. Quy trình TS-DOM-API cố định "Content-Type: application/json" (bước 3). | Header được cố định trong quy trình như hằng số, không được xét là biến đầu vào. |
| TC-FR15-212 (30 POST song song) — *SV đã bỏ ở 5/7d* | EC56 thêm đúng 1 bản ghi (TC-17). | Không xét đồng thời. Quy trình API gửi đúng một request mỗi case. |
| TC-FR15-213 (body PUT có thêm `id`, `role`) | EC57 sửa hợp lệ (TC-19). | Body của AI chỉ gồm 5 khoá theo api_specification. Không xét khoá thừa trong body. |
| TC-FR15-214 (price = `1e-324`) | EC19 ≤ 0; điểm LB−1 = 0 (TC-67, 79, 101, 113). | Giá trị 0 đã kiểm nhưng chỉ dưới dạng `0`. Không xét số JSON bị làm tròn về 0. |
| TC-FR15-216 (alt khi tên có `&`, `"`, `<`) — *SV đã bỏ ở 5/7c* | TC-93 (alt không rỗng, dữ liệu seed), TC-94 (tên `<i>…</i>`, SEC-04). | Hai thuộc tính được kiểm riêng, mỗi cái một nơi. AI không kết hợp chúng (escape trong **thuộc tính** alt). |

## Nguyên nhân chung (AI tự nhận)

- **Prompt và cách dẫn bước:**
  - Bước 3 yêu cầu minimum set (một đại diện mỗi lớp). Vì vậy các giá trị khác trong cùng lớp không được chọn: giá âm cực đại, mảng, cách viết khác của số.
  - Quy ước "thuộc tính chung khẳng định ở đúng một case" khiến SEC-04 và alt chỉ có một case mỗi loại.
- **Mô hình miền:**
  - Biến được rút từ FR-15, FR-12.2 và các trường form/API. Thao tác lặp, đồng thời, nhiều tab, trạng thái form trước thao tác, header HTTP, khoá thừa trong body và body không phải JSON không phải "biến" trong mô hình đó, nên không được phân lớp.
- **Giới hạn công cụ:**
  - AI không chạy SUT ở bước 1–4, chỉ đọc mã.
  - Hành vi của parser (input type=number, JSON, Number) không được thử thật.
- **Quy tắc tự đặt:**
  - C4 và C10 do AI đề xuất đã chủ động né (cắt khoảng trắng) hoặc loại trừ (id không tồn tại ở UI) thay vì đưa ra cho SV chốt.
- **Không mang bài học từ feature trước:**
  - Nhiều case SV ở đây cùng kiểu với case SV của B_FR07: `1e5`, số 0 đứng đầu, `Infinity`, `1e-324`, mảng, Content-Type, đồng thời, bấm liên tục, nhiều tab, 2^53.
  - Ở bước 1–4 của C_FR15, AI không đọc `HW02/B_FR07/sv_cases.md` hay `HW02/B_FR07/ai_gap_answer.md`; AI chỉ đọc chúng khi dựng khung `sv_cases.md`, sau bước 4. Không có dẫn chứng nào cho thấy AI đã xét các kiểu case này cho C_FR15.

## Cập nhật sau 5/7c

- **Case SV đã bỏ** (giữ khoảng trống số, lý do ghi trong notes của suite TS-SV-*):
  - TC-203, TC-216, TC-217: Expected không có căn cứ SRS.
  - TC-204: kèm theo C19 bị bỏ.
  - Các dòng của 4 case này trong bảng trên được giữ lại làm lịch sử và đánh dấu "SV đã bỏ".
- **Sau 5/7c còn 14 case SV.** Nhóm 1: 200, 208, 215. Nhóm 2: 201, 202, 205, 206, 207, 209, 210, 211, 212, 213, 214. Nhóm 3: không có.

### TC-FR15-200 so với TC-FR15-94 (dữ kiện)

| Mục | TC-FR15-94 (AI, TS-GUI) | TC-FR15-200 (SV, TS-SV-UI) |
|---|---|---|
| Đường nhập | POST /api/products bằng token admin | Form 'Thêm sản phẩm mới' trên UI |
| Giá trị tên | `<i>SEC04 {ts}</i>` | `<script>alert(1)</script>` |
| Điểm quan sát | Ô 'Tên SP' trong bảng: chữ hiển thị nguyên văn, không có phần tử `<i>` con | Bảng hiển thị dạng chuỗi văn bản; không bật alert; kết quả lưu ("Thêm thành công (hoặc báo lỗi/escape)") |
| Căn cứ | SEC-04, C12 | SEC-04, C12, C21 |

- **Phần trùng:** cả hai kiểm SEC-04 cho tên sản phẩm hiển thị trong bảng sản phẩm.
- **TC-200 thêm:**
  - dữ liệu đi qua form UI (TC-94 đi qua API);
  - payload thực thi được, quan sát được bằng hộp thoại alert;
  - quan sát kết quả lưu khi tạo (C21).
- **TC-94 có mà TC-200 không ghi:** kiểm cấu trúc DOM của ô (không có phần tử con được render từ chuỗi).

## Cập nhật sau 5/7d

- **Case SV đã bỏ thêm** (giữ khoảng trống số):
  - TC-210: không có lớp tương ứng.
  - TC-212: Expected không có căn cứ SRS.
  - TC-215: SV bỏ sau khi xét lại C1/C2.
- **Sau 5/7d còn 11 case SV.** Nhóm 1: 200, 208. Nhóm 2: 201, 202, 205, 206, 207, 209, 211, 213, 214. Nhóm 3: không có.
- **TC-200:** Expected đổi thành "Báo lỗi; tuyệt đối không kích hoạt alert XSS (SEC-04, C21)". Vì vậy ở bảng so sánh với TC-94 phía trên, điểm quan sát "kết quả lưu" của TC-200 giờ là bị từ chối. Phần trùng với TC-94 (hiển thị tên trong bảng) không còn được quan sát ở TC-200, vì không có bản ghi nào được tạo.

