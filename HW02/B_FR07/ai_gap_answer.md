# B_FR07 – AI trả lời "vì sao bản AI không có case này" (bước 5)

Đây là câu trả lời của AI (Claude Opus 5.5, Claude Code) khi SV hỏi sau khi SV đã tự thêm case. Nó không phải phần phân tích gap của report; phần đó do SV viết.

**Bản đối chiếu:**
- Bản đóng băng bước 3: `HW02/appendix/ai-outputs/B_FR07_step3_20261020-1037.json` (lần đầu) … `-1102.json`.
- Bản đóng băng bước 4: `B_FR07_step4_20261020-111050.json` (bản cuối, 49 TC).
- Dẫn chứng phụ là các output AI trước đó: bước 2 `B_FR07_step2_20261020-1031.json` và `HW02/B_FR07/notes_step1.md`.

**Cách xếp nhóm:**
- **Nhóm 1 – Đã nghĩ tới nhưng không đưa vào:** chỉ khi có dẫn chứng trong output AI rằng chính ý hoặc giá trị đó đã được xét.
- **Nhóm 2 – Không nghĩ tới:** không có dẫn chứng nào. Với nhóm này, AI vẫn ghi lớp EC gần nhất mà bản AI đã có, để thấy case SV khác ở chỗ nào. Điều đó không có nghĩa AI đã nghĩ tới case.

## Nhóm 1 – Đã nghĩ tới nhưng không đưa vào

| Case SV | Dẫn chứng trong output AI | Vì sao không có trong bản bước 3–4 |
|---|---|---|
| TC-FR07-205 (đổi Số lượng giữa hai lần bấm thêm ở trang chi tiết) | `notes_step1.md:74`: "lần bấm đầu ở trang chi tiết không gọi `addToCart` (`ProductDetail.jsx:21–31`)", xếp vào "ghi nhận trung lập, chưa kết luận, chờ bước 6". Lớp EC9 (thêm lại từ cùng trang) được phủ bởi TC-FR07-03: CT id 5 × 1 rồi CT id 5 × 3, về trang chủ giữa hai lần (bản step4-111050). | AI tự đặt quy tắc không dùng mã SUT làm nguồn yêu cầu, nên ghi nhận này không được chuyển thành case. Minimum set đã có TC-03 phủ EC9 nên không thêm case. TC-03 đi qua trang chủ giữa hai lần thêm và không kiểm phản hồi sau lần thêm đầu, nên không có trình tự "ở lại trang, đổi số, bấm lại" như case SV. |
| TC-FR07-207 (name chứa HTML/XSS qua API) | Bước 2: EC32 "API: body.name khác tên CSDL (kể cả chuỗi chứa thẻ HTML)" và yêu cầu SEC-04 (escape). Bản step3-1037: TC-FR07-23 có name = `"<b>Hack</b>"`, Expected là giỏ dùng tên CSDL. | EC32, TC-23 và SEC-04 bị gỡ trong vòng sửa bước 3 thứ nhất theo lệnh từ phiên thảo luận. Từ bản step3-1102 trở đi không còn. Oracle của AI (tên lấy từ CSDL, theo B8) cũng khác oracle của SV (sanitize/escape). |
| TC-FR07-210 (price âm cực lớn qua API) | Bản step4-111050: EC16 có tên lớp "API: body.price khác giá CSDL (khác số, ≤ 0, sai kiểu, thiếu)". Bước 2, giả định B8: "Nếu SV chọn chấp nhận giá client → tách thêm lớp không hợp lệ (price ≤ 0 …)". | Theo B8 (giá lấy từ CSDL), mọi price client gửi thuộc cùng một lớp hợp lệ EC16. AI chọn một đại diện duy nhất là price = 1 (TC-FR07-22), theo quy tắc một đại diện/lớp của minimum set. Giá âm đã được nêu trong tên lớp nhưng không thành case riêng. |

## Nhóm 2 – Không nghĩ tới

| Case SV | Lớp gần nhất mà bản AI có | Ghi chú nguyên nhân |
|---|---|---|
| TC-FR07-200 (chuỗi `<script>` vào ô Số lượng UI) | EC5 "Không phải số", đại diện `'abc'` (TC-FR07-13). Notes TC-13 có nói ô type=number có thể không nhận chữ. | Bản AI coi mọi chuỗi không phải số là một lớp và chọn `'abc'`. Khía cạnh thực thi script ở ô này không xuất hiện trong output nào: SEC-04 ở bước 2 chỉ áp cho tên sản phẩm hiển thị. |
| TC-FR07-201 (bấm 'Thêm vào giỏ' 20 lần liên tục) | EC37 cộng dồn (TC-03, TC-04, thêm lại 1 lần). | Mô hình miền của AI xét từng lần thao tác đơn lẻ. Không có biến nào về số lần hay tốc độ thao tác. |
| TC-FR07-202 (2 tab cùng user) | EC17 '+', EC21 xoá (TC-05, TC-08). B0d chỉ ghi giỏ là state React, mất khi tải lại. | Không có biến về nhiều phiên hoặc nhiều tab. Quy trình UI của AI giả định một tab, một browser context mỗi case. |
| TC-FR07-203 (`1e5` vào ô Số lượng) | EC1 (đại diện 2), EC5 (`'abc'`). BVA: 0, 1, 2, 5, 1000. | Không xét cách viết khác của cùng một giá trị số (ký hiệu số mũ mà input type=number cho gõ). |
| TC-FR07-204 (localStorage hỏng rồi F5) | EC26/EC27 trạng thái đăng nhập. V8 ghi token nằm trong localStorage (AuthContext.jsx). | localStorage chỉ được ghi làm nguồn quan sát. Không có lớp nào cho dữ liệu lưu trữ bị hỏng. Tải lại trang bị B10 đưa ra ngoài phạm vi. |
| TC-FR07-206 (`007`) | EC1 số nguyên ≥ 1, đại diện 2. | Không xét định dạng chuỗi của số hợp lệ (số 0 đứng đầu). |
| TC-FR07-208 (`1e-324`, JSON đọc thành 0) | EC2 ≤ 0. Điểm LB-1 = 0 ở TC-FR07-70. | Giá trị 0 đã kiểm, nhưng chỉ dưới dạng `0`. Không xét cách biểu diễn số JSON bị làm tròn về 0. |
| TC-FR07-209 (`Infinity` thô trong body) | EC5 / EC6 / EC7 (quantity sai kiểu, chuỗi, thiếu). Lớp V20 EC51. | Không xét body không phải JSON hợp lệ. Mọi case API của AI gửi JSON hợp lệ. |
| TC-FR07-211 (id là mảng) | EC13 "id sai kiểu", đại diện `"abc"` (TC-FR07-37). | Lớp có, nhưng không có dẫn chứng AI đã xét kiểu mảng. Một đại diện chuỗi được coi là đủ cho cả lớp. |
| TC-FR07-212 (id là object) | Như TC-211. | Như TC-211. |
| TC-FR07-213 (50 POST song song) | EC37 cộng dồn, EC11 (POST lần 2 cùng id, TC-FR07-21). | Không xét đồng thời. Quy trình API của AI gửi đúng một POST mỗi case. |
| TC-FR07-214 (Content-Type: text/plain) | EC51. Quy trình TS-DOM-API cố định "Content-Type: application/json". | Header được cố định trong quy trình như một hằng số. Không được xét như một biến đầu vào. |
| TC-FR07-215 (quantity = 2^53 + 1) | EC1, giá trị lớn 1000 nhãn LARGE (TC-FR07-74), theo B1 không có cận trên. | AI đã nghĩ tới phía "giá trị lớn" nhưng chỉ chọn 1000 làm đại diện. Không có dẫn chứng AI đã xét giới hạn độ chính xác của Number trong JavaScript. |

## Nguyên nhân chung (AI tự nhận)

- **Prompt và cách dẫn bước:**
  - Mỗi bước được dẫn theo đúng kỹ thuật domain/BVA, và bước 3 yêu cầu minimum set (một đại diện mỗi lớp). Vì vậy các giá trị khác trong cùng lớp (mảng/object, giá âm, `<script>`, `1e5`, `007`) không được chọn.
  - Các lệnh sửa của phiên thảo luận thu hẹp phạm vi: gỡ EC32/SEC-04, đưa B10 ra ngoài phạm vi.
- **Mô hình miền:**
  - Biến được rút từ đặc tả FR-06/07/08 và trường form/API. Thao tác lặp, đồng thời, nhiều tab, dữ liệu lưu trữ hỏng và header HTTP không phải "biến" trong mô hình đó, nên không được phân lớp.
- **Giới hạn công cụ:**
  - AI không chạy SUT ở bước 1–4, chỉ đọc mã.
  - Hành vi của parser (JSON, input type=number, Number) không được thử thật, nên không lộ ra các giá trị có cách biểu diễn đặc biệt.
- **Quy tắc tự đặt:**
  - Ghi nhận từ mã SUT (ProductDetail.jsx:21–31) bị giữ ở mức "chờ bước 6" để không dùng code làm oracle. Hệ quả là trình tự thao tác lộ ra ghi nhận đó không thành case.
