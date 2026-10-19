# Prompt Log – HW02
**Họ tên:** Lê Tấn Hiệp | **MSSV:** 23120255 | **Công cụ AI:** Claude Opus 5.5, Claude Sonnet 4.6

> Prompt và output được trích tự động, nguyên văn, từ transcript của công cụ AI bằng script `tools/extract_prompt_log.py` (không qua AI). Section, Mục đích và Xử lý do em tự ghi.

---

## #1 | 21:20 12/10/2026 | Claude Sonnet 4.6 | Toàn bài
**Mục đích:** [...]

**Prompt:**
```
Đọc context và kinh nghiệm rút ra từ session khác của homework môn software testing nhé
```
*Đính kèm:* `attachment.txt` (context và bài học HW01)

**Output:**
```
Đã đọc xong. Từ HW02 mình sẽ làm theo bộ quy tắc này. Mấy điểm mình sẽ giữ chặt nhất:

- **Vai trò:** góp ý ngắn, thẳng, làm từng bước. Không viết hộ AI Impact Analysis, Critique hay prompt log. Không gợi ý edge case trước khi bạn tự tìm (G9.3). Không cài lỗi vào artifact. Không bịa nguồn. Không tick hộ AI-05.
- **Quy trình:** đọc đề, chỉ ra chỗ mâu thuẫn hoặc dễ sót, lập dàn ý có 🔒/📝/`[...]`, làm từng Requirement, rồi viết Audit, Critique và Disclosure, điền form, cuối cùng rà nhất quán.
- **Test case:** Expected phải có oracle và ngưỡng Pass/Fail trước khi chạy. Tiêu đề TC trung lập. Mỗi TC ghi kỹ thuật thiết kế và lý do chọn input. Có bảng truy vết. Căn cứ ghi theo "tài liệu ISTQB (v4.0.1) của môn học, chương X".
- **Đầu ra:** file `.md` kèm danh sách "đã sửa gì / bạn cần tự làm gì". Excel cập nhật thêm dòng vào file cũ, giữ 3 sheet và dùng công thức.
- **Rủi ro 0 điểm:** mình sẽ chủ động báo khi số lượt AI, số artifact, tỉ lệ hoặc Disclosure không khớp giữa report, Phụ lục A và AI-02/03/05. Lượt AI làm việc phụ (form, Excel, sửa nhất quán) cũng được tính là artifact.

Có hai việc cần làm sớm ở HW02, vì HW01 đã vướng:
1. **Hỏi thầy xem Mantis có bắt buộc không** trước khi quyết định bỏ.
2. **EShop SUT:** mình cần biết bạn chạy bản nào (link repo/deploy, môi trường local hay server của thầy) thì Expected mới có oracle đúng.

Gửi đề HW02 (và tài liệu EShop nếu có), mình bắt đầu từ bước tóm tắt bảng điểm và liệt kê chỗ dễ sót.
```

**Xử lý:** [...]

---

## #2 | 21:25 12/10/2026 | Claude Sonnet 4.6 | [...]
**Mục đích:** [...]

**Prompt:**
```
Đọc yêu cầu đề giúp mình nhé
```
*Đính kèm:* `2026.HW02.Domain Testing_En.md`

**Output:**
```
## Bảng điểm

| Mục | Điểm | Ghi chú |
|---|---|---|
| Feature A (Domain + BVA) | 25 | Chọn 1 FR trong FR-01…06 |
| Feature B | 25 | Chọn 1 FR trong FR-07…11 |
| Feature C | 25 | Chọn 1 FR trong FR-12…19 |
| Feature D (Mobile) | 15 | Đề **không liệt kê FR** cho Pool D |
| Agent Skills | 10 | Có kèm video YouTube |

**Khác HW01:** bảng điểm không có cột AI compliance. Audit Report, Critique và commit log nằm trong danh sách nộp bắt buộc, mà §17 ghi "thiếu tài liệu bắt buộc → **0 điểm cả bài**". Rủi ro vì vậy còn nặng hơn HW01.

## Chỗ mâu thuẫn hoặc dễ sót

1. **Pool D trống.** Phải xem repo `eshop-sut` có app mobile và spec không, và chạy được bằng gì (emulator, Expo…). 15 điểm phụ thuộc vào việc này.
2. **Agent Skill:** §2 và §7 ghi "encouraged" nhưng chiếm 10 điểm. Thực tế là bắt buộc nếu muốn điểm tối đa. Video demo end-to-end phải do bạn tự quay và thuyết minh.
3. **Prompt log và quy tắc HW01.** §9 khuyến khích *"tạo skill/rule tự trích xuất tool, thời gian, prompt, output sau session"*, và §11 Anti-AI-Cheat = **None**. Điều này mâu thuẫn với quy tắc "AI không viết prompt log" rút ra từ HW01, vốn có thể là ràng buộc riêng của HW01. Bạn nên quyết định (hoặc hỏi thầy) trước khi bắt đầu. Cho tới khi bạn chốt, mình vẫn giữ quy tắc cũ.
4. **Biểu mẫu AI-02/03/05:** đề chỉ ghi "use the given AI Templates **if needed**". Vì có luật 0 điểm, an toàn nhất là vẫn làm và ký như HW01.
5. **Excel incremental:** đề HW02 không nhắc đến. Test summary bắt buộc phải nằm trong **`README.md`**: số feature, số TC thiết kế, đã chạy, Pass, Fail, chưa chạy, số bug, link video. Nếu vẫn giữ Excel thì số liệu hai nơi phải khớp.
6. **Phải chạy test thật**, vì summary có executed/passed/failed. Cần dựng SUT local sớm.
7. **Bug báo ở 2 nơi:** trong report .md và trên **GitHub Issues của nhóm**. Mỗi issue có ảnh đính kèm, và zip còn phải có ảnh chụp trang Issues. Cần repo nhóm và quyền tạo issue.
8. **Commit chi tiết hơn HW01:** mỗi bước kỹ thuật × mỗi feature. Ví dụ: phân tích biến → phân vùng → TC Domain → TC BVA → chạy → bug → gap analysis. Tính ra ~4 × 6–7 commit.
9. **Tên zip mới:** `23120255_HW02_AI_DomainTesting_<grade>.zip`, không còn là `HWxx_AI_<grade>`.
10. **Định dạng:** report, Audit và Critique đều cần **cả .md lẫn PDF**.
11. **AI gap analysis (G9.3):** giữ quy trình cũ. AI sinh TC trước, bạn tự tìm chỗ thiếu, sau đó mới hỏi AI vì sao bỏ sót. Phải phân loại nguyên do: prompt, giới hạn tool, hay độ phức tạp của feature.
12. **Chống trùng:** 4 feature không được trùng với thành viên khác trong nhóm, và **chép prompt cũng bị 0 điểm cả hai bên**. Đừng dùng chung prompt hoặc skill với bạn cùng nhóm.
13. **"Domain testing" theo bài giảng:** đề nhấn mạnh hai lần "review the course lectures". Cách trình bày từng bước (bảng biến, equivalence class, on/off/in/out point…) nên bám đúng slide của thầy.
14. **Nộp trễ không được nhận**, deadline xem trên Moodle. Thời lượng dự kiến 10 giờ cho 4 feature, khá chặt.

## Mình cần từ bạn

- 4 feature nhóm đã phân cho bạn (hoặc danh sách feature còn trống).
- Slide hoặc tài liệu Domain Testing và BVA của thầy.
- Deadline trên Moodle và link repo nhóm (cho GitHub Issues).
- Quyết định về điểm 3 (prompt log tự động hay tự ghi).

Bước tiếp theo, mình có thể đọc repo `eshop-sut` để xác nhận Pool D, cách chạy SUT, và spec của các FR bạn chọn.
```

**Xử lý:** [...]

---

## #3 | 21:26 12/10/2026 | Claude Sonnet 4.6 + Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
https://github.com/ttbhanh/eshop-sut
---
Xem repo rồi chọn giúp mình các feature dễ Test nhất trong các pool nhé
```

**Output:**
```
Mình sẽ clone repo, đọc spec và code của các FR rồi đề xuất mỗi pool 1 feature.

Mình đã clone và đọc README (SRS v2.0), `api_specification.md`, `setup_guide.md`, danh sách route backend, các màn hình mobile và form admin.

**Tiêu chí chọn:** input có biên rõ trong SRS (số, độ dài, ngưỡng), ít phụ thuộc trạng thái, chạy được qua UI và ít setup.

## Đề xuất

| Pool | Chọn | Vì sao dễ | Dự phòng nếu bạn cùng nhóm đã lấy |
|---|---|---|---|
| A | **FR-04 Hồ sơ cá nhân** | Một form, 3 trường. SĐT có biên rõ: bắt đầu bằng `0`, dài 10–11 chữ số. Có thêm ràng buộc email không sửa được và `role`. Không cần dữ liệu chuẩn bị. | FR-01 Đăng ký (miền mật khẩu nhiều chiều, nhiều TC hơn) |
| B | **FR-09 Mã giảm giá** | Ví dụ BVA kinh điển: `total >= min_order_amount`, `expired_at`, `max_uses_per_user`. Có sẵn 4 coupon mẫu với ngưỡng 300k và 500k. | FR-07 Giỏ hàng (biên của số lượng, nhưng mỏng) |
| C | **FR-15 Product CRUD** | Biên rõ: tên bắt buộc và tối đa 255 ký tự, giá > 0, danh mục bắt buộc. Form admin đơn giản. | FR-17 Coupon CRUD (nhiều trường hơn nên nhiều TC hơn) |
| D | **Mobile – Hồ sơ (FR-20 + FR-04)** | Dùng lại mô hình miền của FR-04, chỉ đổi nền tảng. Có thể so sánh web và mobile. | Mobile – Coupon ở Checkout (dùng lại FR-09) |

## Lưu ý

- **FR-09 cần dữ liệu biên.** 5 sản phẩm seed đều ≥ 4.000.000₫, không tạo được tổng 299.999 / 300.000 / 300.001. Bạn phải dùng admin (FR-15) tạo sản phẩm có giá đúng biên. Đây cũng là lý do FR-15 hợp: phần setup của B nằm sẵn trong C. Coupon còn bị tiêu lượt dùng, nên phải chạy lại `node database.js` để reset giữa các lần.
- **Mobile tốn setup nhất.** `API_URL` trong `frontend-mobile/App.js` đang hard-code IP `192.168.10.13`, nên phải đổi sang IP LAN của máy bạn. Thay đổi này cần ghi vào mục môi trường test. Cần Expo Go (SDK 54) hoặc emulator, và điện thoại phải chung Wi-Fi với máy. Nên dựng thử ngay tối nay.
- **Tài khoản admin:** README ghi `Admin123!`, `setup_guide.md` ghi `admin123`. Seed DB dùng `Admin123!`.
- **Agent Skill (10đ):** cả 4 feature đều có dạng "validate trường nhập", nên một skill Domain + BVA dùng được cho tất cả. Video demo cũng dễ quay.
- **Rủi ro:** feature dễ thì cũng dễ bị chấm "mỏng", mà đề nói rõ chấm *quality over completion*. FR-04 cần được mở rộng hết các trường (tên, địa chỉ, email, `role` qua API) để đủ chất liệu cho 25 điểm.
- **Mình không liệt kê bug.** Khi đọc code có thể đã thấy vài chỗ, nhưng mình cố ý không nói, để phần tìm bug và AI gap analysis là của bạn. Mình chỉ đánh giá dựa trên spec.

Lượt này (chọn feature) là một lượt AI cần ghi vào prompt log.

Bạn chốt 4 feature với nhóm xong thì báo mình. Bước tiếp theo là dựng dàn ý report và cây thư mục HW02.
```

**Xử lý:** [...]

---

## #4 | 21:28 12/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Hiện tại trong nhóm mình đã có người chọn:
A - FR-04: Personal profile management
B - FR-09: Discount coupons
C - FR-14: Category management (CRUD)
D - Tương tự C
===
Nên nếu như trùng feature thì giúp mình chọn lại cái feature khác trong pool đó mà cũng dễ demo nhé. Hmm, mình nghĩ sẽ chọn Feature D giống như ở feature C để demo giống nhau. Bạn có nghĩ vậy không?
```

**Output:**
```
Ý tưởng dùng chung một feature cho 2 nền tảng là tốt, nhưng **không áp dụng được với C**. Pool C là Web Admin, còn app mobile chỉ có các màn: Home/tìm kiếm, Chi tiết SP, Giỏ hàng, Checkout, Đăng nhập, Đăng ký, Quên mật khẩu, Hồ sơ. Mobile không có quản lý danh mục hay sản phẩm, nên không thể test FR-14/FR-15 trên mobile. (Nếu "D tương tự C" của bạn cùng nhóm nghĩa là category trên mobile thì họ cũng sẽ vướng chỗ này.)

Nên áp dụng ý tưởng đó cho **A**:

| Pool | Chọn | Lý do |
|---|---|---|
| A | **FR-01 Đăng ký** | Không cần setup. Miền rõ: email đúng định dạng và duy nhất, mật khẩu ≥ 8 ký tự và đủ 4 loại ký tự, xác nhận mật khẩu phải khớp. Nhiều chiều nên có đủ chất liệu cho 25 điểm. |
| B | **FR-07 Giỏ hàng** | Dễ demo nhất trong phần còn lại. Biên chính là số lượng (nút −/+ quanh 1) và quy tắc thêm trùng sản phẩm thì tăng số lượng. **Điểm yếu:** SRS không có cận trên, nên miền mỏng hơn. Bạn sẽ phải tự định nghĩa và ghi rõ giả định (ví dụ số lượng lớn, giá trị âm hoặc 0 qua API `POST /api/cart`). |
| C | **FR-15 Product CRUD** | Chưa ai lấy. Biên rõ: tên tối đa 255 ký tự, giá > 0, danh mục bắt buộc. Gần FR-14 của bạn kia nhưng không trùng. |
| D | **Mobile – Đăng ký** (FR-20 + FR-01) | Dùng lại mô hình miền của A, chỉ đổi nền tảng. So sánh web và mobile cùng input là chất liệu tốt cho phần phân tích. |

Lý do không chọn các feature khác ở Pool B: FR-08 thiên về bảo mật (`total_amount` từ client), FR-10 là state transition, FR-11 gần như không có input. Cả ba đều khó áp domain/BVA một cách tự nhiên.

Hai việc cần chốt với nhóm:
1. Pool D có tính trùng theo **chức năng** không (ví dụ người khác cũng chọn "Mobile – Đăng ký")? Cách an toàn là ghi rõ D của bạn là *"FR-20 – chức năng Đăng ký trên mobile"*.
2. Bạn kia nên kiểm tra lại D của họ, vì mobile không có tính năng admin.

Chốt xong thì mình làm tiếp dàn ý report và cây thư mục HW02.
```

**Xử lý:** [...]

---

## #5 | 21:30 12/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
mình thấy trước đó Pool C bạn backup FR-17 mà, tại sao lại đổi sang FR-15 vậy?
```

**Output:**
```
Mình không đổi. Ở lượt trước, **FR-15 là lựa chọn chính** của Pool C, còn FR-17 chỉ là dự phòng trong trường hợp FR-15 đã có người lấy. Bạn cùng nhóm chọn FR-14, nên FR-15 vẫn còn trống và mình giữ nguyên.

Nếu bạn đang phân vân giữa hai cái:

| | FR-15 Product CRUD | FR-17 Coupon CRUD |
|---|---|---|
| Số trường có ràng buộc | 3 (tên ≤ 255, giá > 0, danh mục) | 6 (`code` duy nhất, `type`, `discount_value` > 0, `expired_at`, `min_order_amount` ≥ 0, `max_uses_per_user` ≥ 1) |
| Công sức | Ít hơn, demo nhanh | Nhiều TC hơn, nhiều chất liệu cho 25 điểm |
| Chỗ mơ hồ cần tự ghi giả định | Ít | Nhiều hơn: SRS không nói `percent` có được vượt 100 hay không, `expired_at` có được là ngày quá khứ hay không |

**Khuyến nghị:**
- Muốn **dễ và chắc** thì chọn FR-15.
- Muốn **miền phong phú hơn** để bù cho FR-07 vốn mỏng thì chọn FR-17. Đổi lại, bạn phải viết thêm giả định cho các chỗ SRS bỏ ngỏ.

FR-17 gần với FR-09 của bạn cùng nhóm, nhưng không tính là trùng: một bên là quản trị coupon (admin CRUD), một bên là áp dụng coupon lúc checkout.
```

**Xử lý:** [...]

---

## #6 | 21:31 12/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Vậy mình ghi Pool D của mình tương tự A được không nhỉ?
```

**Output:**
```
Được, nhưng nên **ghi cụ thể** thay vì viết "tương tự A". Ví dụ:

> **Feature D:** FR-20 – Chức năng **Đăng ký trên Mobile** (áp dụng yêu cầu FR-01)

Cách ghi này rõ cho người chấm và tránh bị hiểu là trùng feature trong nhóm.

Để D đủ giá trị 15 điểm và không bị coi là copy của A:

- **Dùng lại** mô hình miền (biến, phân lớp, giá trị biên) của A, và ghi rõ "kế thừa từ mục A".
- **Chạy lại toàn bộ TC trên app mobile**, với TC ID riêng (ví dụ `D-xx`), Actual riêng và ảnh chụp từ điện thoại hoặc emulator. Không lấy kết quả web sang.
- **Bổ sung phần riêng của mobile:** đối chiếu xem UI mobile có đủ các trường và thông báo lỗi mà SRS yêu cầu không, cách nhập trên bàn phím ảo (dán chuỗi dài, khoảng trắng đầu/cuối), và ghi rõ môi trường (Expo Go hay emulator, phiên bản, IP backend đã đổi).
- **Thêm một bảng so sánh web và mobile** cho cùng input. Chỗ nào hai bên xử lý khác nhau thì đó là chất liệu tốt cho phần phân tích.

Còn một việc: báo nhóm để không ai chọn trùng "Đăng ký trên Mobile".
```

**Xử lý:** [...]

---

## #7 | 21:31 12/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Nhưng tại sao không làm FR-15 nhỉ?
```

**Output:**
```
FR-15 vẫn là lựa chọn của bạn cho **Pool C**. Nó chỉ không làm được ở **Pool D**, vì app mobile **không có chức năng quản trị**.

Trong `frontend-mobile/App.js` chỉ có các màn sau: `home`, `productDetail`, `cart`, `checkout`, `login`, `register`, `forgotPassword`, `profile`. Mobile không có màn thêm, sửa hay xóa sản phẩm, nên không có UI nào để test FR-15. SRS cũng nói vậy: FR-20 chỉ liệt kê Xem sản phẩm, Đăng nhập, Đăng xuất, Đăng ký, Giỏ hàng, Thanh toán, Hồ sơ, Lịch sử đơn hàng.

Chỉ những feature Pool A hoặc B có màn tương ứng trên mobile mới "nhân đôi" được sang D. Vì vậy D đi theo A (Đăng ký), không đi theo C.

Bộ chốt của bạn:
- **A:** FR-01 Đăng ký
- **B:** FR-07 Giỏ hàng
- **C:** FR-15 Product CRUD
- **D:** FR-20 – Đăng ký trên Mobile
```

**Xử lý:** [...]

---

## #8 | 21:33 12/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
ủa vậy FR-14 kia có trên mobile không nhỉ?
```

**Output:**
```
Không có. Mình tìm trong `frontend-mobile/App.js` các từ "category" và "danh mục" thì **không có kết quả nào**. App mobile không quản lý danh mục, và cũng không hiển thị danh mục sản phẩm.

Như vậy nếu "D tương tự C" của bạn cùng nhóm là FR-14 trên mobile thì **không làm được**. Bạn nên báo họ sớm. Họ cũng phải chọn D theo một chức năng mobile có thật, tức là một trong các màn: Home/tìm kiếm, Chi tiết SP, Giỏ hàng, Checkout, Đăng nhập, Đăng ký, Quên mật khẩu, Hồ sơ. Đồng thời họ không được trùng với "Đăng ký trên Mobile" của bạn. Với họ, hợp lý nhất là **Hồ sơ trên Mobile**, vì nó khớp với FR-04 họ đang làm ở A.
```

**Xử lý:** [...]

---

## #9 | 14:06 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Lần trước, khi tôi thực hiện HW01, tôi đặt file HW01 vào trong repo này: https://github.com/ThachHaoo/software-testing-2627
Vậy theo bạn, giờ tôi nên clone HW02 ra riêng, hay là clone HW02 vào trong repo này rồi xoá file .git, rồi thực hiện tương tự không?
===
Nhắc lại là các pool mình chọn như này nhé: 
A - 	FR-01: Đăng ký
B - 	FR-07: Giỏ hàng
C - 	FR-15: Product CRUD
D -  FR-20: Đăng ký trên Mobile
===
Giờ bắt đầu thực hiện HW02 nào. Đầu tiên là hỗ trợ mình thiết lập môi trường nhé 
/cs423-ai-first-homework
```

**Output:**
````
Mình sẽ nạp skill của môn, xem repo HW01 rồi đề xuất cách tổ chức HW02 và các bước dựng môi trường.

## 1. Đặt HW02 ở đâu

**Để HW02 trong repo `software-testing-2627`, nhưng không chép EShop vào repo đó.** Clone EShop ra một thư mục riêng, giữ nguyên `.git` của nó.

```
D:\CS423\
├── software-testing-2627\   ← repo bài nộp (HW01\, HW02\ …)
└── eshop-sut\               ← SUT, clone riêng, không commit vào repo bài nộp
```

Lý do:
- **SUT không phải bài nộp.** Chép vào sẽ kéo theo `node_modules` và `database.sqlite`, zip dễ vượt 20 MB.
- **Backend xoá và seed lại DB mỗi lần `node server.js` chạy**, vì `database.js` tự gọi `initDatabase()`. Nếu SUT nằm trong repo bài nộp, file `.sqlite` sẽ đổi liên tục và làm bẩn commit log.
- **Cách cũ (xoá `.git` của EShop) làm mất khả năng xem mình đã sửa gì.** Mobile bắt buộc phải sửa `API_URL`. Còn `.git` thì bạn xuất được thay đổi bằng `git diff > ...\HW02\env\mobile_api_url.patch` để nộp làm bằng chứng.
- Trong report chỉ cần ghi phiên bản SUT: commit **`85af3ba`** (15/05/2026).

Bug thì báo trên **GitHub Issues của repo nhóm**, không phải repo này.

## 2. Biểu mẫu AI cho HW02

| Mã | Cần không | Ghi chú |
|---|---|---|
| AI-02 Audit Report | **Bắt buộc** | Đề §9, cần cả .md và PDF |
| AI-03 Disclosure | Bắt buộc | |
| AI-04 Reflective | Không cần | Chỉ dành cho project, seminar, đồ án |
| AI-05 Privacy | Bắt buộc | Làm cuối cùng |
| AI-06 | Đã nộp tuần 1? | Kiểm tra lại ngày ký |
| Mantis | **Thay bằng GitHub Issues** | Theo đề HW02 |
| Excel | Đề không yêu cầu | Test summary đặt trong `README.md` |

## 3. Dựng môi trường (Windows, PowerShell)

Mình đã chạy thử backend và build web trên Node 22: chạy ổn với commit `85af3ba`.

**Chạy trên Windows, không chạy trong WSL2.** Điện thoại cần kết nối tới backend và Metro qua IP LAN, mà WSL2 dùng NAT nên sẽ chặn kết nối đó.

```powershell
node -v        # cần >= 20.19 (Vite 8 và Expo 54 yêu cầu). Khuyên dùng Node 22 LTS
cd D:\CS423
git clone https://github.com/ttbhanh/eshop-sut.git
cd eshop-sut; git rev-parse --short HEAD   # phải ra 85af3ba
```

Mở 4 terminal:

```powershell
# T1 – Backend :3000 (không cần chạy `node database.js`, server tự seed)
cd backend; npm install; node server.js

# T2 – Web :5173
cd frontend-web; npm install; npm run dev

# T3 – Admin :5174  (đăng nhập admin@eshop.com / Admin123!)
cd frontend-admin; npm install; npm run dev

# T4 – Mobile
ipconfig       # lấy IPv4 của card Wi-Fi (không lấy địa chỉ 100.x của Tailscale)
# sửa frontend-mobile\App.js dòng 16: const API_URL = "http://<IP-của-bạn>:3000/api";
cd frontend-mobile; npm install; npx expo start
```

**Kiểm tra mobile từng bước:**
1. Trên điện thoại, mở trình duyệt vào `http://<IP>:3000/api/products`. Thấy JSON nghĩa là mạng thông. Nếu không thấy:
   - Đặt Wi-Fi của máy là mạng **Private**.
   - Cho phép Node.js qua Windows Firewall.
   - Wi-Fi trường thường chặn các máy trong mạng thấy nhau. Khi đó dùng **hotspot của điện thoại**.
2. Quét QR bằng Expo Go. Nếu Expo Go báo không hợp SDK: dự án dùng **SDK 54**, còn Expo Go trên store có thể đã lên bản mới hơn. Hai cách xử lý:
   - Cài Expo Go bản cho SDK 54 (Android có trang tải bản cũ trên expo.dev).
   - Dùng Android Emulator: trong `expo start`, bấm `a`, Expo sẽ tự cài bản Expo Go phù hợp.

   Mình không kiểm tra được thiết bị của bạn, nên cần bạn thử thực tế.

**Smoke test** (không phải test case, chỉ để biết môi trường chạy được):
- Web: trang chủ có 5 sản phẩm, đăng nhập được bằng `test@eshop.com`.
- Admin: thấy tab Products.
- Mobile: thấy danh sách sản phẩm.

## 4. Đặc điểm môi trường cần ghi vào report

Đây là đặc điểm môi trường, không phải bug, nhưng sẽ quyết định cách bạn viết precondition:
- **Mỗi lần restart backend, mọi thứ bị reset:** tài khoản đã đăng ký, sản phẩm admin tạo, và giỏ hàng (giỏ chỉ nằm trong RAM, ở biến `userCarts`).
  - Tốt: FR-01 test lại được cùng một email.
  - Phải để ý: FR-07 và FR-15 sẽ mất dữ liệu đã tạo nếu lỡ restart giữa chừng.
- Tài khoản admin: README ghi `Admin123!`, `setup_guide.md` ghi `admin123`. Dữ liệu seed dùng `Admin123!`.
- Bảng môi trường cần có: OS, Node, trình duyệt, điện thoại và phiên bản OS, phiên bản Expo Go, commit SUT, IP backend đã đổi.

## 5. Bạn cần làm

1. Chạy các bước trên rồi báo lỗi nếu có. Riêng mobile, nên thử ngay vì đây là phần dễ vướng nhất.
2. Gửi link **repo nhóm** (nơi tạo GitHub Issues).
3. Tạo `HW02\` trong repo, thêm thư mục `env\` chứa file patch, rồi commit đầu tiên kiểu `HW02: khởi tạo thư mục và ghi nhận môi trường test`.
4. Lượt này (thiết lập môi trường) cũng tính là một lượt AI trong prompt log.

Môi trường chạy được thì mình dựng dàn ý report và cây thư mục HW02.
````

**Xử lý:** [...]

---

## #10 | 14:53 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Tôi đã tự fork về group của nhóm và chạy ra:
PS D:\HK7\Testing\Exercise\HW> cd eshop-sut; git rev-parse --short HEAD   # phải ra 85af3ba
85af3ba
===
Đã thử hết các bước trên. đăng nhập admin được. dùng mobile vào trang ra json; quét qr không được, sau khi xuống bản SDK 54 thì đã làm được.
===

2.  https://github.com/tkob-team/eshop-sut
3. Đã xong
4. Oke

===
Thầy mình bảo là, thời đại này càng lười là càng tốt. Tức là có thể tạo các bộ skills hoặc hệ thống harness để AI có thể làm được càng nhiều, con người tham gia càng ít thì càng tốt. Vậy nên trong lúc làm bạn thấy cái gì mà Agent có thể hỗ trợ được (như Claude Code), thì gợi ý cho mình nhé. Có thể viết thêm skills, tạo hệ thống Harness để thực hiện. Rồi mình chỉ tham gia đánh giá, review, chỉnh sửa nếu cần nhé.
Bạn xem bài nộp HW01: https://github.com/ThachHaoo/software-testing-2627. Xem có cần tham khảo gì từ nó không nhé.
/cs423-ai-first-homework
```

**Output:**
```
## 1. Từ HW01: giữ gì, đổi gì

**Giữ nguyên:**
- Header: họ tên, MSSV, cấp độ AI, công cụ, link repo.
- Audit Report:
  - bảng nối mã A với prompt #n và verdict;
  - đủ 5 mục cho mỗi artifact;
  - bảng tỉ lệ verdict, kèm phần nên và không nên dùng AI;
  - bảng đánh giá từng TC do AI sinh.
- Disclosure 4 đoạn (AI tạo / em sửa / em bổ sung / em tự viết), kèm danh mục cấm.
- Tự đánh giá có cột căn cứ và checklist.
- Thư mục `appendix/ai-outputs/` không sửa, Phụ lục A dạng bảng tóm tắt.

**Phải đổi:**
- **Commit:** HW01 có 19 commit, message chung chung ("update log", "Finish HW1"). HW02 yêu cầu mỗi bước của mỗi feature một commit, nên cần quy ước kiểu `HW02[A-FR01] 3/7: TC Domain`. Tổng khoảng 30 commit.
- **README:** README gốc của repo chỉ có tiêu đề. HW02 bắt buộc có `HW02/README.md` gồm bảng tự đánh giá, test summary và link video.
- **Expected và Actual:** ở HW01, Actual của TC02, TC05, TC06 gần như chép lại Expected, còn TC03 ghi "ghi lại thời gian" mà không có ngưỡng. Ở HW02, Actual nên là giá trị quan sát được: HTTP status, thông báo lỗi, URL sau khi submit.
- **Prompt log:** viết tay 23.700 từ là phần tốn công nhất và dễ sai giờ nhất. Phần này nên tự động hoá (H1 bên dưới).
- **Excel:** bỏ, vì đề HW02 không yêu cầu.

⚠️ **Repo `software-testing-2627` đang public**, mình clone được mà không cần đăng nhập. HW02 có luật chép prompt thì 0 điểm cả hai bên, mà Agent Skill thực chất là prompt. Nên chuyển repo sang private tới khi qua deadline.

⚠️ **Fork `tkob-team/eshop-sut`:** GitHub tắt Issues trên fork theo mặc định. Vào Settings → Features → tick **Issues**.

## 2. Đề xuất harness

**Nguyên tắc:** agent làm phần lặp lại và tính toán. Bạn giữ phần được chấm là của người (G9.3, AI-01 §11) và phần phải tự giải thích khi vấn đáp.

| # | Thành phần | Agent làm | Bạn làm |
|---|---|---|---|
| H1 | Trích prompt log | Script đọc transcript của session (`.jsonl`) rồi xuất `A_prompt_log.md` đúng format HW01: #n, giờ thật, prompt và output nguyên văn. Script lọc bỏ các khối hệ thống (có email, memory). Mình đã kiểm tra: transcript của session này có đủ dữ liệu. | Điền cột Mục đích và Xử lý, rà lại một lượt |
| H2 | **Agent Skill `domain-bva-testing`** (10đ) | Viết skill theo các bước trong bài giảng: biến → phân vùng → on/off/in/out → TC có oracle → bảng truy vết. Output gồm .md và YAML | Đưa slide của thầy; 🔒 quay video demo có thuyết minh |
| H3 | Chạy test web/admin | Sinh test Playwright (UI) và test API từ file YAML, chạy thử trước khi giao | Chạy trên máy bạn, để screenshot và kết quả mang hostname của bạn |
| H4 | Tổng hợp số liệu | Script điền Actual/Verdict và summary trong README từ file kết quả, nên số liệu luôn khớp | Duyệt verdict |
| H5 | Commit và commit log | Commit đúng quy ước sau mỗi bước, xuất log | — |
| H6 | GitHub Issues | Tạo issue bằng `gh issue create` từ file bạn viết, kèm ảnh | 🔒 Viết mô tả bug (AI-01 §11 cấm AI viết nháp) |
| H7 | Rà soát trước khi nộp | Skill `hw-submission-audit` và script đếm số lượt AI, số artifact | Ký form |
| H8 | Xuất PDF | Chuyển hàng loạt .md sang PDF | — |

**Không tự động hoá:**
- tự tìm TC còn thiếu trước khi hỏi AI;
- phân tích vì sao AI bỏ sót;
- AI Critique;
- mô tả bug;
- video;
- ký form;
- test mobile: FR-20 nên chạy tay trên Expo Go. Maestro cũng làm được nhưng cần emulator, không đáng công cho 15 điểm.

**Luồng một feature (7 commit):**
1. Phân tích biến.
2. Phân vùng.
3. TC Domain.
4. TC BVA. (Output AI của bước 1–4 lưu vào `ai-outputs/` và không sửa.)
5. 🔒 Bạn tự tìm TC còn thiếu, rồi hỏi AI vì sao bỏ sót.
6. Chạy script để có Actual và Verdict.
7. 🔒 Viết bug và tạo Issue.

**Hai chỗ quy định không khớp nhau, cần biết:**
- Quy ước từ HW01 là "AI không viết prompt log", nhưng HW02 §9 lại khuyến khích skill hoặc rule tự trích xuất log. H1 là script trích nguyên văn, không phải AI viết lại, nên mình nghĩ nó hợp với đề HW02. Dù vậy phải khai rõ trong Disclosure. Muốn chắc chắn thì hỏi thầy một câu.
- AI-01 §11 yêu cầu "SV tự viết boundary case", còn HW02 R2 cho phép "BVA với sự hỗ trợ của AI". Bước 5 trong luồng giải quyết chỗ này: AI viết nháp, bạn bổ sung các biên AI bỏ sót và ghi rõ nguồn.

## 3. Bạn chốt giúp mình

1. **H1:** dùng script trích xuất, hay tự ghi như HW01?
2. **Agent chạy ở đâu:**
   - **(a) Tiếp tục session này.** Mình dựng harness và push lên repo, nên bạn cần cấp quyền push vào `software-testing-2627`. Script test vẫn chạy trên máy bạn.
   - **(b) Claude Code trên máy bạn.** Chạy được SUT, test và commit trực tiếp. Mình chuẩn bị sẵn `CLAUDE.md` và skill để bạn chép vào.

   Mình gợi ý (a) cho đến khi dựng xong harness, vì transcript của session này cũng là nguồn cho prompt log.
3. **Gửi slide Domain Testing và BVA của thầy.** H2 và các bước 1–4 phải bám đúng cách thầy dạy (cách đặt tên on/off point, mẫu bảng).
```

**Xử lý:** [...]

---

## #11 | 15:07 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
1. H1: Có thể dùng để trích xuất, xong rồi điền theo format trước đó của mình được không? Chứ tự ghi nhiều prompt quá, trong khi có thể tự động hoá được.
2. Mình nghĩ là (b), vì mình nghĩ ở session ở những lần bạn fork, clone về môi trường của bạn mình không thể thấy được.
3. Oke

Đồng thời, mình đưa bạn thêm skill mà thầy gửi cho lớp mình nhé. Đọc qua, tham khảo có thể lấy về và cải tiến thêm gì cho Testing tổng quát của mình không nhé.
```
*Đính kèm:* `test-case-writing.skill`, `EN.DOMAIN_TESTING.pdf`, `EN.DOMAIN_TESTING_-_UC_Analysis.pdf`, `S04_Domain_Testing.pdf`

**Output:**
````
Now render the full log with a sample notes file to check the output format.

## 1. H1: Trích prompt log (đã xong)

Được, script trích nguyên văn prompt và output, giữ đúng format HW01 (`## #n | HH:MM dd/mm/yyyy | Tool | Section`, rồi Mục đích, Prompt, Output, Xử lý). Script không dùng AI. Phần đánh giá vẫn do bạn ghi, trong file `prompt_log_notes.toml` (Section, Mục đích, Xử lý); chạy lại script không làm mất các ghi chú này.

```powershell
# 1. Xem danh sách lượt để biết số #n
python tools\extract_prompt_log.py "$env:USERPROFILE\.claude\projects\<thư-mục-repo>\*.jsonl" --since 2026-10-12 --list
# 2. Ghi chú vào prompt_log_notes.toml, rồi xuất log
python tools\extract_prompt_log.py "...\*.jsonl" --since 2026-10-12 --notes HW02\appendix\prompt_log_notes.toml --title "Prompt Log – HW02" -o HW02\appendix\A_prompt_log.md
```

- Cần Python 3.11 trở lên (máy bạn đã có 3.11).
- Script tự lọc các khối hệ thống, kể cả email và memory. Mình đã kiểm tra trên session này: không lọt ra ngoài.
- Lượt dùng Gemini, ChatGPT… thì thêm vào file `--extra`. Script đánh số chung theo thời gian.

Ba việc cần lưu ý:
- **Session này nằm trên cloud.** Bạn không đọc được transcript của nó từ máy mình. Khi xong việc ở đây, nhắn mình "xuất prompt log", mình sẽ chạy script và gửi file cho bạn.
- **Transcript ghi #1, #2 và một phần #3 là Claude Sonnet 4.6**, các lượt còn lại là Claude Opus 5.5. Bạn kiểm tra lại. Nếu đúng thì AI-03 phải khai cả hai model.
- **Khai báo:** ghi trong Disclosure rằng "prompt log được trích tự động bằng script, phần Section/Mục đích/Xử lý em tự ghi". Bản thân script cũng là một artifact do AI tạo, nên phải có một dòng trong Audit.

## 2. Skill `test-case-writing` của thầy

**Nên lấy:**
- **Schema JSON làm nguồn dữ liệu duy nhất.** Nó có sẵn `origin` (Human/AI/Both, khớp cột Nguồn), `covers` (lớp hoặc biên mà TC nhắm tới) và `assumptions`. Mình sẽ dùng schema này làm xương sống cho harness: một file JSON sinh ra cả bảng .md, script Playwright và số liệu README.
- **Linter:** bắt được các cụm mơ hồ tiếng Việt như "thông báo lỗi phù hợp", và bắt TC thiếu bước dọn dẹp.
- **Rubric 0–2 × 7 thuộc tính** để chấm từng TC của AI. Đây là bảng đánh giá từng TC mà Audit đang cần.

**Cần lưu ý:**
- Skill xuất ra Word và Excel, nhưng Homework Policies yêu cầu nộp .md và không dùng Word. Mình sẽ viết thêm phần xuất .md; Excel không bắt buộc.
- Skill để AI viết toàn bộ test case, kể cả case biên. Trong môn này AI-01 §11 vẫn áp dụng: bản nháp của AI phải lưu nguyên, phần bạn bổ sung đánh dấu `origin: Human`.
- Skill có nhắc tới một skill đi kèm là `domain-testing-design`, nhưng thầy không gửi. Bạn hỏi thầy xem có bản đó không.
- Cài file `.skill` của thầy nguyên bản để giữ cả thư mục scripts.

## 3. Slide quyết định cấu trúc report

Mỗi feature đi theo 4 bước, ra đúng 4 bảng như slide:

| Bước | Bảng | Thuộc yêu cầu |
|---|---|---|
| 1. Biến vào/ra | Danh sách Input/Output | R1 |
| 2. Lớp tương đương | Complete Set of Partitions (EC1…) | R1 |
| 3. Chọn TC | Coverage of Partitions và Minimum Set (lớp hợp lệ gộp nhiều lớp vào một TC; lớp không hợp lệ mỗi TC chỉ một lớp) | R1 Domain |
| 4. Biên | Boundary Value TC: LB−1, LB, LB+1, UB−1, UB, UB+1, các biến khác giữ nominal; thêm min/max nhập được qua UI | R2 BVA |

Mô hình biên ở đây là **mô hình 9 điểm của slide**, khác cách 2-value/3-value của ISTQB. Làm theo slide và ghi rõ trong report.

## 4. Card cải tiến `test-design-istqb`

Các thay đổi chính:
- thêm mục Domain/BVA theo 4 bước của bài giảng;
- quy tắc đặt tiêu đề Action + Function + Condition;
- hai định dạng matrix và step-by-step;
- 7 thuộc tính và rubric chấm, ánh xạ sang VALID/INCOMPLETE/INVALID;
- danh sách giả định, bước dọn dẹp, nguyên tắc một nguồn JSON.

Mọi nội dung cũ đều giữ lại. Ví dụ trong skill mình cố ý lấy từ lĩnh vực khác (đặt phòng, quạt), để skill không gợi ý sẵn edge case cho các FR của bạn.

## Tiếp theo

Mình dựng gói harness cho Claude Code trên máy bạn:
- `CLAUDE.md`: các quy tắc AI-01, luồng 7 bước, quy ước commit;
- skill `domain-bva-testing` (bài nộp 10đ, theo 4 bước của slide, dùng schema của thầy);
- `tc_json_to_md.py`;
- khung Playwright cho web/admin và API, kèm script gộp kết quả vào JSON;
- `summary.py` cho README;
- `export_commit_log.ps1`.

Bạn chỉ cần chép gói vào repo và review. Skill `cs423-ai-first-homework` hiện vẫn ghi "AI không viết prompt log". Nếu bạn muốn, mình sẽ đề xuất sửa dòng đó cho khớp với cách dùng script mới.
````
*File AI ghi/gửi trong lượt này:* `extract_prompt_log.py`, `test-design-istqb.SKILL.md`, `prompt_log_notes.toml`

**Xử lý:** [...]

---

## #12 | 15:20 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Được, giúp mình đổi AI không viết prompt log, và đổi lại nhé (vì viết prompt log thì mình suy nghĩ có thể dùng tools được code để trích xuất và thêm vào, chứ không nhất thiết dùng AI).
Gói Harness cho Claude Code không biết có các skill ở session này không nhỉ? Và đưa đầy đủ context làm bài tập để nó thực hiện nhé. Cũng như nhớ cả prompt log,...
===
2 file Extract-prompt-log.py và prompt-log-notes.toml này mình nên làm gì đây?
```

**Output:**
```
Now I'll build the harness package. First, the project context file for Claude Code.

Now the scripts: check, render, freeze, merge.

Now I'll test the hook end to end against this session's transcript, plus the summary script.

Now the setup guide, then package everything.

I've built the harness package (`harness-HW02.zip`). I updated the course skill in the card above, and my edits are only in the prompt-log section.

## 1. Skill `cs423-ai-first-homework` (card above)

- Removed "prompt log" from the list of things AI may not create.
- Added a rule: AI may not write, rewrite or hand-edit any prompt log content.
- The log now comes from one of two sources: you write it yourself, or a script extracts it verbatim from the transcript. AI may write and run that script.
- Added a "Prompt log" section to §5, and updated the AI-03 form and the Mandatory Disclosure to state how the log was produced.
- Noted that for HW02, bugs go to GitHub Issues as the assignment says.

I left `hw-submission-audit` unchanged. Its rule "don't edit the prompt log" still fits: if the log is wrong, you re-run the extraction instead of editing it.

## 2. Will Claude Code have the skills from this session?

**Usually yes, if you sign in to Claude Code with your claude.ai account (not an API key).** According to the docs, Claude Code automatically syncs your account's skills to `~/.claude/skills/synced/`, which requires a fairly recent version. Run `/skills` to check: you should see a **claude.ai sync** group.

The two skills that may not be synced are packaged directly into the repo under `.claude/skills/`:
- `domain-bva-testing`: the Agent Skill for the 10 points;
- `test-case-writing`: your teacher's skill, left unchanged.

## 3. What's in the package

| File | Purpose |
|---|---|
| `CLAUDE.md` | Full context for Claude Code: your info, the HW02 brief and rubric, the 4 features, SUT details (commit, ports, accounts, DB reset on restart, mobile patch), decisions made so far, the 7-step workflow per feature with commit messages, the limits on what AI may do, and commands |
| `.claude/settings.json` | **Stop hook** that rebuilds the prompt log after each Claude turn. It keeps transcripts for 365 days and blocks Claude from editing `ai-outputs/` and `A_prompt_log.md` directly |
| `domain-bva-testing` | One step of the 4-step slide method per call; it stops after BVA so you can add test cases yourself. Scripts: `check_domain.py` checks partition coverage and the one-invalid-class-per-test-case rule; `render_md.py` outputs the 4 tables in the slide format; `freeze.py` freezes the AI draft; `merge_results.py` merges Playwright results and copies screenshots into `evidence/` |
| `tools/` | Prompt-log extractor, `summary.py` (writes the summary table into the README), `export_commit_log.ps1`, `hw.toml` (config for the current homework) |
| `context/` | HW02 brief, HW01 lessons (updated with the new prompt-log rule). Put the slide PDFs in `context/private/`; it is gitignored |
| `HW02/` | Folder skeleton, README with self-assessment table, environment template, Playwright config |
| `HARNESS_SETUP.md` | Step-by-step setup |

What I tested here:
- The hook on this session's transcript: 12 turns, no system text or email leaked.
- `check_domain`, the teacher's linter and `render_md` on the slide example: 0 errors.
- `merge_results` with a real Playwright run.

What I couldn't test: Windows itself (the hook calls `python`, so `python --version` must be ≥ 3.11) and the Claude Code `/hooks` and `/skills` screens.

## 4. About `extract_prompt_log.py` and `prompt_log_notes.toml`

**Don't use those two loose files.** The package already has them in the right places (`tools/` and `HW02/appendix/`), and the hook runs the script for you. What's left for you:

1. **Fill in the notes file** `HW02/appendix/prompt_log_notes.toml`, with Section / Purpose / Handling for each turn #n. To see the #n list, run the `--list` command.
2. **Copy the cloud session's transcript** (the one running right now) into `.transcripts/` in the repo. When you're done working here, message me "xuất transcript" and I'll send the `.jsonl` file. Fill in the notes after copying it, because adding an older session renumbers the turns.

## Notes

- **Declare the whole harness in the Audit.** `CLAUDE.md`, the skill and the scripts are all AI-built artifacts.
- **Don't push `.transcripts/`.** It contains system text. `.gitignore` already blocks it.
- Before you start, make the repo private and enable Issues on the fork.
```
*File AI ghi/gửi trong lượt này:* `SKILL.md`, `schema-domain.md`, `automation.md`, `check_domain.py`, `render_md.py`, `freeze.py`, `merge_results.py`, `hw.toml`, `on_stop.py`, `summary.py`, `export_commit_log.ps1`, `CLAUDE.md`, `HARNESS_SETUP.md`, `harness-HW02.zip`

**Xử lý:** [...]

---

## #13 | 15:40 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
Vậy giờ mình tải file zip này về, extract ra rồi đặt từng file ở đâu nhỉ? Mà eshop-sut fork về mình đã mở issues rồi nhé. Nhưng không đổi sang private được.
===
1 cái nữa là: có lẽ mình sẽ muốn prompt ở session này nhiều hơn, do có nhiều context hơn. Và session này mình muốn kiểu là nơi để thảo luận, brainstorm, hướng dẫn làm. Còn ở Claude Code kiểu như là người thực hiện những cái mà bạn không làm được. Hoặc là chạy nguyên harness để thực hiện test,...
Bạn thấy vậy ổn không? Cần cải tiến thêm không?
```

**Output:**
````
## 1. Giải nén vào đâu

Giải nén **toàn bộ** file zip vào **gốc repo** `software-testing-2627`, cùng cấp với `HW01/`. Không cần chép từng file. Gói này không có file nào trùng với repo hiện tại (repo chỉ có `README.md` và `HW01/`).

```powershell
cd D:\HK7\Testing\Exercise\HW\software-testing-2627   # chỉnh lại theo đường dẫn thật
Expand-Archive -Path "$HOME\Downloads\harness-HW02.zip" -DestinationPath . -Force
git status            # phải thấy: CLAUDE.md, HARNESS_SETUP.md, .gitignore, .claude/, tools/, context/, HW02/
```

Thư mục `.claude` và file `.gitignore` bắt đầu bằng dấu chấm nên Explorer có thể ẩn đi. Dùng `git status` để chắc chắn đã có đủ. Sau đó bỏ 3 file PDF slide vào `context\private\` và làm tiếp theo `HARNESS_SETUP.md` mục 4.

Hãy dùng **bản zip mới nhất** (tin nhắn này). Bản này thêm phần vai trò của Claude Code, nói ở mục 3 bên dưới.

## 2. Không chuyển được sang private

Có hai trường hợp:

- **Nếu bạn thử với fork `eshop-sut`:** GitHub không cho đổi fork của repo public sang private. Fork này cũng không cần private. Repo cần private là **`software-testing-2627`**.
- **Nếu chính `software-testing-2627` không đổi được** (repo thuộc tài khoản `ThachHaoo`, có thể bạn không có quyền admin): cách đơn giản nhất là **chỉ commit trên máy, `git push` sau hạn nộp**. Commit vẫn giữ giờ gốc, và commit log được xuất từ máy nên không ảnh hưởng bài nộp. Mình đã ghi cách này vào CLAUDE.md.

## 3. Chia vai hai phiên: ổn, kèm 4 điểm cần thêm

Cách chia này hợp lý. Phiên này giữ context dài để thảo luận và review. Claude Code làm phần cần chạy trên máy bạn, gồm SUT, test, commit, ảnh có hostname.

Bốn điểm cần thêm:

1. **Cầu nối giữa hai phiên (đã thêm vào CLAUDE.md).**
   - Khi cần Claude Code làm gì, mình sẽ viết một khối **"Lệnh cho Claude Code"** để bạn dán sang.
   - Claude Code làm xong sẽ in khối **"Báo cáo cho phiên thảo luận"** (file đã sửa, kết quả check/test, commit, câu hỏi). Bạn dán khối đó ngược lại đây.
   - Quyết định chốt ở đây thì mình đưa kèm dòng để thêm vào mục "Quyết định đã chốt" trong CLAUDE.md.
2. **Transcript của phiên này có thể mất.** Phiên này chạy trong container cloud, có thể bị thu hồi khi không hoạt động lâu. Cuối mỗi buổi làm, nhắn "xuất transcript" để mình gửi file `.jsonl`, bạn bỏ vào `.transcripts/`. Xuất nhiều lần cũng được, script tự gộp và không đếm trùng lượt.
3. **Lượt AI ở cả hai phiên đều tính vào log.** Thảo luận ở đây cũng là một lượt AI. Script sẽ gộp hai nguồn theo thời gian. Lúc ghi chú Section/Mục đích, bạn nên ghi rõ lượt đó là "thảo luận" hay "thực hiện". Ghi như vậy giúp phần Audit tự nhiên hơn.
4. **Bước 5 (tự tìm TC còn thiếu) vẫn là phần của bạn, ở cả hai phiên.** Phiên này có nhiều context hơn nên càng dễ lỡ gợi ý. Khi bạn đang ở bước 5, mình sẽ chỉ hỏi ngược lại hoặc chỉ ra kỹ thuật, không đưa ra case cụ thể.

Một lựa chọn để cân nhắc: nếu bạn mở cuộc trò chuyện này trong app Claude desktop và chọn liên kết với máy tính, phiên này đọc được trực tiếp `testcases.json` và kết quả test trên máy bạn, không cần dán qua lại. Vai trò vẫn giữ nguyên: Claude Code chạy, phiên này review.

Việc tiếp theo: bạn cài harness xong và chạy bước kiểm tra trong `HARNESS_SETUP.md` (`/skills`, `/hooks`, `on_stop.py --manual`), báo lại kết quả. Sau đó mình viết khối lệnh đầu tiên cho Claude Code: bước 0–1 của FR-01.
````
*File AI ghi/gửi trong lượt này:* `harness-HW02.zip`

**Xử lý:** [...]

---

## #14 | 15:55 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
PS D:\HK7\Testing\Exercise\HW\software-testing-2627> git status            # phải thấy: CLAUDE.md, HARNESS_SETUP.md, .gitignore, .claude/, tools/, context/, HW02/
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .claude/
        .gitignore
        HARNESS_SETUP.md
        HW02/A_FR01/
        HW02/B_FR07/
        HW02/C_FR15/
        HW02/D_FR20/
        HW02/README.md
        HW02/ai-forms/
        HW02/appendix/
        HW02/bugs/
        HW02/env/environment.md
        HW02/tests/
        context/
        tools/

nothing added to commit but untracked files present (use "git add" to track)
===
Hình như CLAUDE.md mình đã không cho push ở máy luôn rồi thì phải. Nếu cần push có thể giúp mình sửa lại nhé.
Đã chuyển sang private, cái repo của mình ròi nhé.
===
Đã add-dir; kiểm tra skills, hooks hợp lệ, và chạy lệnh ra như sau:
PS D:\HK7\Testing\Exercise\HW\software-testing-2627> python tools/hooks/on_stop.py --manual
PS D:\HK7\Testing\Exercise\HW\software-testing-2627> 
===
bạn bảo commit rồi làm bài nhưng mình chưa thấy CLAUDE.md nên muốn hỏi ý kiến bạn trước khi commit nhé
```

**Output:**
```
(không có output dạng văn bản)
```
*File AI ghi/gửi trong lượt này:* `on_stop.py`, `claude-ai_session_HW02.jsonl`

**Xử lý:** [...]

---

## #15 | 16:10 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<command-message>domain-bva-testing</command-message>
<command-name>/domain-bva-testing</command-name>
<command-args>HW02/A_FR01 0
Xong bước 0 thì làm tiếp bước 1 cho cùng feature.

Feature: FR-01 Đăng ký tài khoản (Pool A, HW02).
Test basis: ../eshop-sut/README.md mục FR-01 (và FR-22 nếu liên quan tới form). SRS là oracle.
Mã nguồn chỉ dùng để lấy đúng tên nhãn, trường, nút, thông báo, endpoint: ../eshop-sut/frontend-web/src/pages/Register.jsx, route POST /api/register trong ../eshop-sut/backend/server.js.
Phạm vi tầng: UI + API  

Yêu cầu:
- Bước 0: tạo HW02/A_FR01/testcases.json. meta.sut_version = "eshop-sut 85af3ba"; meta.references ghi file + dòng đã đọc; tách FR-01 thành các yêu cầu có mã FR-01.1, FR-01.2…
- Bước 1: domain.variables gồm cả biến đầu vào và biến đầu ra; cột source ghi đúng nơi biến xuất hiện.
- Chỗ nào SRS không nói rõ thì ghi vào meta.assumptions, không tự quyết ngầm.
- Chạy: freeze.py --step 1 --note "Claude Code bước 0-1", check_domain.py, render_md.py -o HW02/A_FR01/testcases.md.
- KHÔNG làm bước 2 trở đi. KHÔNG commit, chờ em review.
- Kết thúc bằng khối "Báo cáo cho phiên thảo luận".</command-args>
```

**Output:**
````
Đã đọc xong test basis (SRS FR-01/FR-22, Register.jsx, route backend, API spec). Giờ xem linter cần trường gì rồi viết JSON.

Viết `testcases.json` (bước 0 + 1).

Lỗi encoding console (cp1252), không phải lỗi dữ liệu. Chạy lại với `PYTHONIOENCODING=utf-8`.

Xong bước 0 và 1 cho FR-01. Chưa commit, chờ em review.

**Bước 0.** `testcases.json` đã có meta và 14 yêu cầu: FR-01.1→FR-01.10 tách từ FR-01, thêm FR-22.1→FR-22.4. `meta.references` ghi 9 nguồn, mỗi nguồn kèm file và dòng. Có 14 giả định A1→A14, tức là mỗi chỗ SRS không nói rõ.

**Bước 1.** Có 9 biến:

| Mã | Biến | Vào/Ra |
|---|---|---|
| V1 | Họ Tên | Vào |
| V2 | Email | Vào |
| V3 | Email đã tồn tại trong hệ thống (trạng thái CSDL) | Vào |
| V4 | Mật khẩu | Vào |
| V5 | Xác nhận mật khẩu | Vào |
| V6 | Thông báo lỗi trên form | Ra |
| V7 | Trang đích sau khi bấm "Đăng Ký" | Ra |
| V8 | Phản hồi API (mã HTTP + body) | Ra |
| V9 | Bản ghi tài khoản trong CSDL | Ra |

Cột `source` chỉ ghi nơi biến xuất hiện. Riêng V5 ghi đúng điều đã đọc: form trong Register.jsx không có ô này, body API cũng không có. Em quyết định có tính là lỗi hay không ở bước 7.

**Lưu ý môi trường:**
- HEAD của repo SUT đang ở `de0f48f`, không phải `85af3ba`. So với `85af3ba` chỉ khác `.gitignore`, `database.sqlite` và `App.js` mobile (dòng `API_URL`). Mã web và backend không đổi, nên em vẫn ghi `sut_version = "eshop-sut 85af3ba"`.
- Script in tiếng Việt ra console Windows bị lỗi `UnicodeEncodeError` (cp1252). Phải chạy với `PYTHONIOENCODING=utf-8`. Em nên thêm biến này vào lệnh mẫu trong CLAUDE.md.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: /domain-bva-testing HW02/A_FR01 bước 0 + bước 1 (FR-01 Đăng ký, tầng UI + API)
- File đã tạo/sửa:
  - HW02/A_FR01/testcases.json (mới: meta, 14 yêu cầu FR-01.1–FR-01.10 + FR-22.1–FR-22.4, 14 giả định A1–A14, 9 biến V1–V9)
  - HW02/A_FR01/testcases.md (sinh bằng render_md.py)
  - HW02/appendix/ai-outputs/A_FR01_step1_20261019-1613.{json,md} + dòng mới trong INDEX.md (freeze, note "Claude Code bước 0-1")
- Kết quả kiểm tra: check_domain 0 lỗi / 5 cảnh báo (cả 5 đều do chưa có partitions → bước 2) · lint 0 lỗi / 14 cảnh báo (chưa có TC phủ yêu cầu → bước 3) · test Not run
- Commit: chưa commit (chờ SV review) → dự kiến "HW02[A-FR01] 1/7: Phân tích biến vào/ra"
- Cần quyết định / câu hỏi:
  1. A3: email trùng có phân biệt hoa/thường không, có cắt khoảng trắng đầu/cuối không? (AI đang giả định: không phân biệt, có cắt)
  2. A5: tập ký tự đặc biệt {@ $ ! % * ? &} có phải tập đóng không? Mật khẩu chỉ có '#' thì bị từ chối?
  3. A8: yêu cầu "xác nhận mật khẩu" chỉ kiểm ở UI, không áp dụng cho API?
  4. A14: FR-22 ('*', type=email, type=password, vị trí lỗi) để ngoài phân lớp, kiểm bằng case GUI riêng — có đưa vào phạm vi không? Có thêm FR-21 (màu nút submit) và SEC-01 (mật khẩu không lưu plaintext, có thể thêm thành biến đầu ra) không?
  5. A1/A4: Họ Tên và Mật khẩu không có cận trên → bước 4 chỉ làm BVA quanh cận dưới. Đồng ý không?
  6. HEAD của repo SUT là de0f48f (chỉ thêm .gitignore so với 85af3ba) → có cần ghi vào environment.md không?
  7. Console Windows cần PYTHONIOENCODING=utf-8 mới chạy được script → đề xuất thêm vào lệnh mẫu trong CLAUDE.md.
```
````
*File AI ghi/gửi trong lượt này:* `testcases.json`

**Xử lý:** [...]

---

## #16 | 16:10 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<command-message>domain-bva-testing</command-message>
<command-name>/domain-bva-testing</command-name>
<command-args>HW02/A_FR01 0
Xong bước 0 thì làm tiếp bước 1 cho cùng feature.

Feature: FR-01 Đăng ký tài khoản (Pool A, HW02).
Test basis: ../eshop-sut/README.md mục FR-01 (và FR-22 nếu liên quan tới form). SRS là oracle.
Mã nguồn chỉ dùng để lấy đúng tên nhãn, trường, nút, thông báo, endpoint: ../eshop-sut/frontend-web/src/pages/Register.jsx, route POST /api/register trong ../eshop-sut/backend/server.js.
Phạm vi tầng: UI + API  

Yêu cầu:
- Bước 0: tạo HW02/A_FR01/testcases.json. meta.sut_version = "eshop-sut 85af3ba"; meta.references ghi file + dòng đã đọc; tách FR-01 thành các yêu cầu có mã FR-01.1, FR-01.2…
- Bước 1: domain.variables gồm cả biến đầu vào và biến đầu ra; cột source ghi đúng nơi biến xuất hiện.
- Chỗ nào SRS không nói rõ thì ghi vào meta.assumptions, không tự quyết ngầm.
- Chạy: freeze.py --step 1 --note "Claude Code bước 0-1", check_domain.py, render_md.py -o HW02/A_FR01/testcases.md.
- KHÔNG làm bước 2 trở đi. KHÔNG commit, chờ em review.
- Kết thúc bằng khối "Báo cáo cho phiên thảo luận".</command-args>
```

**Output:**
````
Đã đọc xong test basis (SRS FR-01/FR-22, Register.jsx, route backend, API spec). Giờ xem linter cần trường gì rồi viết JSON.

Viết `testcases.json` (bước 0 + 1).

Lỗi encoding console (cp1252), không phải lỗi dữ liệu. Chạy lại với `PYTHONIOENCODING=utf-8`.

Xong bước 0 và 1 cho FR-01. Chưa commit, chờ em review.

**Bước 0.** `testcases.json` đã có meta và 14 yêu cầu: FR-01.1→FR-01.10 tách từ FR-01, thêm FR-22.1→FR-22.4. `meta.references` ghi 9 nguồn, mỗi nguồn kèm file và dòng. Có 14 giả định A1→A14, tức là mỗi chỗ SRS không nói rõ.

**Bước 1.** Có 9 biến:

| Mã | Biến | Vào/Ra |
|---|---|---|
| V1 | Họ Tên | Vào |
| V2 | Email | Vào |
| V3 | Email đã tồn tại trong hệ thống (trạng thái CSDL) | Vào |
| V4 | Mật khẩu | Vào |
| V5 | Xác nhận mật khẩu | Vào |
| V6 | Thông báo lỗi trên form | Ra |
| V7 | Trang đích sau khi bấm "Đăng Ký" | Ra |
| V8 | Phản hồi API (mã HTTP + body) | Ra |
| V9 | Bản ghi tài khoản trong CSDL | Ra |

Cột `source` chỉ ghi nơi biến xuất hiện. Riêng V5 ghi đúng điều đã đọc: form trong Register.jsx không có ô này, body API cũng không có. Em quyết định có tính là lỗi hay không ở bước 7.

**Lưu ý môi trường:**
- HEAD của repo SUT đang ở `de0f48f`, không phải `85af3ba`. So với `85af3ba` chỉ khác `.gitignore`, `database.sqlite` và `App.js` mobile (dòng `API_URL`). Mã web và backend không đổi, nên em vẫn ghi `sut_version = "eshop-sut 85af3ba"`.
- Script in tiếng Việt ra console Windows bị lỗi `UnicodeEncodeError` (cp1252). Phải chạy với `PYTHONIOENCODING=utf-8`. Em nên thêm biến này vào lệnh mẫu trong CLAUDE.md.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: /domain-bva-testing HW02/A_FR01 bước 0 + bước 1 (FR-01 Đăng ký, tầng UI + API)
- File đã tạo/sửa:
  - HW02/A_FR01/testcases.json (mới: meta, 14 yêu cầu FR-01.1–FR-01.10 + FR-22.1–FR-22.4, 14 giả định A1–A14, 9 biến V1–V9)
  - HW02/A_FR01/testcases.md (sinh bằng render_md.py)
  - HW02/appendix/ai-outputs/A_FR01_step1_20261019-1613.{json,md} + dòng mới trong INDEX.md (freeze, note "Claude Code bước 0-1")
- Kết quả kiểm tra: check_domain 0 lỗi / 5 cảnh báo (cả 5 đều do chưa có partitions → bước 2) · lint 0 lỗi / 14 cảnh báo (chưa có TC phủ yêu cầu → bước 3) · test Not run
- Commit: chưa commit (chờ SV review) → dự kiến "HW02[A-FR01] 1/7: Phân tích biến vào/ra"
- Cần quyết định / câu hỏi:
  1. A3: email trùng có phân biệt hoa/thường không, có cắt khoảng trắng đầu/cuối không? (AI đang giả định: không phân biệt, có cắt)
  2. A5: tập ký tự đặc biệt {@ $ ! % * ? &} có phải tập đóng không? Mật khẩu chỉ có '#' thì bị từ chối?
  3. A8: yêu cầu "xác nhận mật khẩu" chỉ kiểm ở UI, không áp dụng cho API?
  4. A14: FR-22 ('*', type=email, type=password, vị trí lỗi) để ngoài phân lớp, kiểm bằng case GUI riêng — có đưa vào phạm vi không? Có thêm FR-21 (màu nút submit) và SEC-01 (mật khẩu không lưu plaintext, có thể thêm thành biến đầu ra) không?
  5. A1/A4: Họ Tên và Mật khẩu không có cận trên → bước 4 chỉ làm BVA quanh cận dưới. Đồng ý không?
  6. HEAD của repo SUT là de0f48f (chỉ thêm .gitignore so với 85af3ba) → có cần ghi vào environment.md không?
  7. Console Windows cần PYTHONIOENCODING=utf-8 mới chạy được script → đề xuất thêm vào lệnh mẫu trong CLAUDE.md.
```
````
*File AI ghi/gửi trong lượt này:* `testcases.json`

**Xử lý:** [...]

---

## #17 | 16:31 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
Áp dụng quyết định review bước 1 cho HW02/A_FR01. Đây là phần em sửa trên bản nháp đã đóng băng: KHÔNG chạy freeze lại.
1. Giả định: A3 = giả định có phân biệt hoa thường và cắt khoảng trắng đầu/cuối. Khi làm ghi rõ giả định và expected của case tuân theo các giả định này, giữ A5, A8; giữ A1/A4 (không có cận trên, MIN_UI/MAX_UI xét ở bước 4).
2. Phạm vi: giữ FR-22.1–22.4, kiểm bằng suite GUI riêng, không phân lớp; bỏ FR-21 và SEC-01 khỏi phạm vi. Ghi lý do vào meta.scope.
3. Tách FR-01.7 thành FR-01.7a (≥1 chữ hoa), FR-01.7b (≥1 chữ thường), FR-01.7c (≥1 chữ số).
4. V6 và A10: bỏ điều kiện "đặt phía trên nút Đăng Ký" khỏi oracle của case nhập liệu; vị trí thông báo lỗi chỉ kiểm ở case FR-22.4.
5. Thêm trường note cho V2 và V5: "Quan sát mã nguồn: [ô Email type=text | form không có ô Xác nhận mật khẩu]. Chưa kết luận lỗi, xác nhận khi thực thi (bước 6)."
6. SUT = fork tkob-team/eshop-sut @ de0f48f (= ttbhanh/eshop-sut 85af3ba + .gitignore, không đổi mã): cập nhật meta.sut_version, HW02/env/environment.md và CLAUDE.md.
7. CLAUDE.md, mục "Quyết định đã chốt": thêm dòng ngày 2026-10-19 cho các mục 1, 2, 6.
8. Chạy check_domain.py và render_md.py. Commit "HW02[A-FR01] 1/7: Phân tích biến vào/ra" gồm testcases.json/.md, file đóng băng bước 1 trong ai-outputs/, CLAUDE.md, environment.md.
Kết thúc bằng khối "Báo cáo cho phiên thảo luận".
</pasted_content id="1f5a">
```

**Output:**
````
Áp dụng sửa vào `testcases.json`.

Giờ cập nhật environment.md và CLAUDE.md.

Note của V2/V5 có trong JSON nhưng `render_md.py` chưa xuất cột note → .md không hiện. Commit đúng danh sách file.

Em đã áp dụng đủ 8 mục review bước 1 cho A_FR01 và commit `4e30b25`. Không chạy freeze lại, nên file đóng băng là bản nháp gốc của AI. check_domain 0 lỗi.

Có 2 điểm em cần biết:
- **Note của V2 và V5 không hiện trong `testcases.md`.** Trường `note` đã có trong JSON, nhưng bảng biến của `render_md.py` chỉ xuất các cột id, tên, Vào/Ra, source, type, constraint.
- **Còn 7 file đã sửa trước đó mà em không đưa vào commit:** `.claude/settings.json`, 4 script trong `domain-bva-testing/scripts/`, `tools/summary.py`, `HW02/appendix/A_prompt_log.md`. Các file này không thuộc nhiệm vụ này, nên vẫn để chưa commit.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: áp dụng review bước 1 cho HW02/A_FR01 (không chạy freeze lại) + commit bước 1/7
- File đã tạo/sửa:
  - HW02/A_FR01/testcases.json:
    - A3 viết lại: so sánh email trùng có phân biệt hoa/thường, có cắt khoảng trắng đầu/cuối; expected tuân theo giả định này
    - A10 và V6: bỏ "phía trên nút Đăng Ký" khỏi oracle của case nhập liệu, vị trí lỗi chỉ kiểm ở FR-22.4
    - A14: suite GUI riêng cho FR-22, không phân lớp
    - meta.scope: giữ FR-22.1–22.4; bỏ FR-21, SEC-01 kèm lý do
    - FR-01.7 tách thành 7a/7b/7c; constraint của V4 cập nhật theo
    - thêm note cho V2 và V5
    - sut_version = tkob-team/eshop-sut @ de0f48f
    - giữ nguyên A1, A4, A5, A8
  - HW02/A_FR01/testcases.md (render lại)
  - HW02/env/environment.md (dòng SUT)
  - CLAUDE.md (dòng SUT ở mục 1 + 3 dòng "Quyết định đã chốt" ngày 2026-10-19 cho các mục 1, 2, 6)
- Kết quả kiểm tra: JSON hợp lệ · check_domain 0 lỗi / 5 cảnh báo (chưa có partitions → bước 2) · lint 0 lỗi / 16 cảnh báo (chưa có TC phủ yêu cầu; 16 vì FR-01.7 đã tách) · test Not run
- Commit: 4e30b25 HW02[A-FR01] 1/7: Phân tích biến vào/ra (7 file: testcases.json/.md, A_FR01_step1_20261019-1613.json/.md, ai-outputs/INDEX.md, CLAUDE.md, environment.md)
- Cần quyết định / câu hỏi:
  1. render_md.py chưa xuất trường note của biến → note V2/V5 chỉ có trong JSON, không có trong .md. Có sửa render_md.py để thêm cột Ghi chú không? (đây là việc phụ, phải khai trong Audit)
  2. ai-outputs/INDEX.md (sổ ghi freeze) đã đưa vào commit vì đi kèm file đóng băng. Nếu không muốn thì báo để tách ra.
  3. 7 file đã sửa nằm ngoài nhiệm vụ này, chưa commit: .claude/settings.json, 4 script trong domain-bva-testing/scripts, tools/summary.py, A_prompt_log.md. Ai sửa, có commit riêng không?
  4. Bước tiếp theo: /domain-bva-testing HW02/A_FR01 2 (phân lớp tương đương).
```
````

**Xử lý:** [...]

---

## #18 | 16:39 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<command-message>domain-bva-testing</command-message>
<command-name>/domain-bva-testing</command-name>
<command-args>HW02/A_FR01 2</command-args>
```

**Output:**
```
Viết `domain.partitions` (50 lớp) và thêm 2 giả định mới cho các lớp tầng API và cho thông báo HTML5.
```

**Xử lý:** [...]

---

**Tổng:** 18 lượt; Claude Sonnet 4.6 3 lượt (#1, #2, #3); Claude Opus 5.5 16 lượt (#3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18). 1 lượt có output từ hơn một model nên được đếm ở cả hai.
