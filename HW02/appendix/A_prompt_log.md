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
````
Viết `domain.partitions` (50 lớp) và thêm 2 giả định mới cho các lớp tầng API và cho thông báo HTML5.

Bước 2 xong: đã phân 50 lớp tương đương (17 hợp lệ, 33 không hợp lệ) cho cả 9 biến, kể cả 4 biến đầu ra. Bản nháp đã đóng băng; check_domain 0 lỗi. Chưa commit, chờ em review.

| Biến | Lớp hợp lệ | Lớp không hợp lệ |
|---|---|---|
| V1 Họ Tên | EC1 chữ không dấu, EC2 có dấu tiếng Việt | EC3 rỗng, EC4 chỉ khoảng trắng, EC5 thiếu/null (API), EC6 sai kiểu (API) |
| V2 Email | EC7 đúng định dạng, EC8 có khoảng trắng đầu/cuối | EC9 rỗng, EC10 thiếu @, EC11 nhiều @, EC12 trước @ rỗng, EC13 sau @ rỗng, EC14 domain không có dấu chấm, EC15 khoảng trắng ở giữa, EC16–17 thiếu/sai kiểu (API) |
| V3 Email đã tồn tại | EC18 chưa có, EC19 chỉ khác hoa/thường | EC20 trùng y hệt, EC21 trùng sau khi cắt khoảng trắng |
| V4 Mật khẩu | EC22 dài ≥ 8, EC25 có chữ hoa, EC28 có chữ thường, EC31 có chữ số, EC33 có ký tự đặc biệt trong tập, EC34 trong tập + ngoài tập | EC23 dài 1–7, EC24 rỗng, EC26/EC27 không có chữ hoa A–Z (EC27: chỉ có chữ hoa có dấu), EC29/EC30 tương tự cho chữ thường, EC32 không có số, EC35 không có ký tự đặc biệt, EC36 chỉ có ký tự ngoài tập, EC37–38 thiếu/sai kiểu (API) |
| V5 Xác nhận mật khẩu | EC39 khớp | EC40 rỗng, EC41 khác ký tự, EC42 chỉ khác hoa/thường |
| V6–V9 (đầu ra) | EC43 không lỗi, EC45 chuyển `/login`, EC47 HTTP 200 + message/id, EC49 tạo 1 user | EC44 có thông báo lỗi, EC46 ở lại `/register`, EC48 HTTP 4xx + error, EC50 không tạo user |

**Cách chia:**
- Mỗi điều kiện của Mật khẩu là một chiều riêng. Mỗi lớp không hợp lệ chỉ vi phạm một điều kiện, các điều kiện khác vẫn thoả, nên ở bước 3 mỗi case không hợp lệ phủ đúng một lớp.
- Mỗi lớp được tách thêm đều có lý do trong cột `note`.
- Thêm 2 giả định:
  - **A15:** ở tầng API, trường bị thiếu, bằng null hoặc sai kiểu thì không hợp lệ (EC5, EC6, EC16, EC17, EC37, EC38).
  - **A16:** bong bóng cảnh báo HTML5 cũng tính là thông báo lỗi trên form.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: /domain-bva-testing HW02/A_FR01 2: phân lớp tương đương
- File đã tạo/sửa:
  - HW02/A_FR01/testcases.json (thêm domain.partitions EC1–EC50; thêm giả định A15, A16)
  - HW02/A_FR01/testcases.md (render lại)
  - HW02/appendix/ai-outputs/A_FR01_step2_20261019-1641.{json,md} + 2 dòng mới trong INDEX.md
- Kết quả kiểm tra: check_domain 0 lỗi / 51 cảnh báo (50 lớp chưa có case phủ + V4 chưa có case BVA → bước 3–4) · lint 0 lỗi / 16 cảnh báo (chưa có TC) · test Not run
- Commit: chưa commit (chờ SV review) → dự kiến "HW02[A-FR01] 2/7: Phân lớp tương đương"
- Cần quyết định / câu hỏi:
  1. A15: có giữ 6 lớp chỉ kiểm ở tầng API (thiếu/null, sai kiểu cho name/email/password) không? Giữ thì bước 3 sẽ có thêm 6 case API.
  2. A16: bong bóng HTML5 có được tính là "thông báo lỗi trên form" không?
  3. EC27/EC30 (chữ hoa/thường có dấu không được tính, theo A6): giữ hay bỏ?
  4. EC8 và EC21 lấy từ giả định A3 (cắt khoảng trắng đầu/cuối). Nếu SV đổi A3 thì phải đổi theo hai lớp này.
  5. EC19 (chỉ khác hoa/thường → coi là email mới) đi theo A3 em chốt (có phân biệt hoa/thường). Xác nhận đúng ý em chưa?
  6. Các lớp email sai định dạng (EC10–EC15) chia theo từng phần của mẫu bị vi phạm. Có muốn gộp bớt cho minimum set gọn hơn không?
```
````

**Xử lý:** [...]

---

## #19 | 16:47 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
Áp dụng review bước 2 cho HW02/A_FR01 (em sửa trên bản đóng băng, KHÔNG freeze lại):
1. Giữ A15 và 6 lớp chỉ có ở API. Giữ EC10–EC15 riêng. Giữ EC27/EC30 theo A6; ghi thêm vào A6: "Expected của EC27/EC30 phụ thuộc giả định này; kết quả lệch được phân tích là SRS mơ hồ trước khi kết luận lỗi".
2. A16: xác nhận. Bổ sung cách quan sát: bong bóng HTML5 không nằm trong DOM → oracle = form không gửi request + ô ở trạng thái :invalid / validationMessage không rỗng.
3. Xác nhận EC19 theo A3. A3 không đổi.
4. Thêm giả định A17: "Nếu form không có ô Xác nhận mật khẩu (xem note V5): case kiểm sự tồn tại của trường → Fail; các case cần nhập V5 ở tầng UI → Blocked kèm mã bug. Không xoá case."
5. Chạy check_domain.py, render_md.py. Commit "HW02[A-FR01] 2/7: Phân lớp tương đương" gồm testcases.json/.md, file đóng băng bước 2 + INDEX.md, A_prompt_log.md.
Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Em đã áp dụng review bước 2 cho A_FR01 và commit `d799b74`. Không freeze lại; check_domain 0 lỗi.

Thay đổi trong `testcases.json`:
- **A6:** thêm câu về EC27/EC30: Expected phụ thuộc giả định này, kết quả lệch được phân tích là SRS mơ hồ trước khi kết luận lỗi.
- **A16:** ghi là SV xác nhận 2026-10-19 và thêm cách quan sát. Bong bóng HTML5 không nằm trong DOM, nên oracle là: form không gửi `POST /api/register`, và ô liên quan ở trạng thái `:invalid` hoặc `validationMessage` không rỗng.
- **A17 (mới):** nếu form không có ô Xác nhận mật khẩu thì case kiểm sự tồn tại của trường → Fail; các case cần nhập V5 ở tầng UI → Blocked kèm mã bug. Không xoá case.
- A3, A15, EC10–EC15, EC19 giữ nguyên như em chốt.

Trong commit, `A_prompt_log.md` chưa có lượt này vì hook Stop chỉ tạo lại log sau khi lượt kết thúc. Bản cập nhật sẽ vào commit của bước 3.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: áp dụng review bước 2 HW02/A_FR01 (không freeze lại) + commit 2/7
- File đã tạo/sửa: HW02/A_FR01/testcases.json (A6 bổ sung, A16 xác nhận + cách quan sát, thêm A17) · testcases.md (render lại)
- Kết quả kiểm tra: check_domain 0 lỗi / 51 cảnh báo (50 EC chưa có case phủ + V4 chưa có BVA → bước 3–4) · lint 0 lỗi / 16 cảnh báo · test Not run
- Commit: d799b74 HW02[A-FR01] 2/7: Phân lớp tương đương (testcases.json/.md, A_FR01_step2_20261019-1641.{json,md}, ai-outputs/INDEX.md, A_prompt_log.md)
- Cần quyết định / câu hỏi:
  1. A_prompt_log.md chưa có lượt này (hook tạo lại log sau khi lượt kết thúc) → sẽ commit kèm bước 3.
  2. Bước tiếp theo: /domain-bva-testing HW02/A_FR01 3 (TS-DOM minimum set). Gợi ý chốt trước: case cho 6 lớp chỉ có ở API và 3 lớp của V5 đặt chung trong TS-DOM, phân biệt bằng trường layer, hay tách suite riêng?
```
````

**Xử lý:** [...]

---

## #20 | 16:51 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
/domain-bva-testing HW02/A_FR01 3
Ràng buộc thêm cho bước này:
- Mỗi case ghi rõ "layer": "UI" hoặc "API". Lớp chỉ có ở API → case API. Lớp ở tầng UI → case UI; chỉ thêm bản API khi lớp đó có ý nghĩa ở cả hai tầng (theo A9).
- Mã TC: TC-FR01-01… cho TS-DOM. Chừa khoảng trống: TS-BVA bắt đầu từ TC-FR01-60, TS-GUI (FR-22) từ TC-FR01-90.
- Tạo luôn suite TS-GUI cho FR-22.1–22.4 (step-by-step, technique "checklist", không gắn EC).
- Oracle theo A10/A16/A17; case UI không hợp lệ kiểm ba điều: thông báo lỗi (cách quan sát theo A16), vẫn ở /register, không tạo user.
- Chạy freeze --step 3, check_domain (phải 0 lỗi, mọi EC đã phủ), lint, render. KHÔNG làm bước 4. KHÔNG commit.
Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Đã nắm schema và linter. Sinh TS-DOM và TS-GUI bằng script Python, chèn vào chỗ `"suites": []` để không đổi định dạng phần còn lại của file.

Bash lỗi khi parse heredoc dài. Ghi script ra file tạm ngoài repo rồi chạy.

Bước 3 xong: TS-DOM có 53 case, TS-GUI có 5 case. Cả 50 EC đều đã có case phủ và không case nào phủ hai lớp không hợp lệ. check_domain 0 lỗi, lint 0 lỗi. Bản nháp đã freeze, chưa commit.

**TS-DOM (TC-FR01-01…53):**

| Mã | Tầng | Nội dung |
|---|---|---|
| 01–02 | UI | 2 case hợp lệ: 01 phủ các lớp hợp lệ chính; 02 gom các lớp tách riêng (EC2, EC8, EC19, EC34) |
| 03–22 | UI | 20 case không hợp lệ cho các lớp có ở cả hai tầng (V1–V4) |
| 23–25 | UI | 3 case V5, chỉ có ở UI (A8) |
| 26–27 | API | 2 case hợp lệ |
| 28–47 | API | Bản API của 20 lớp không hợp lệ ở trên (theo A9) |
| 48–53 | API | 6 lớp chỉ có ở API (A15) |

**Oracle:**
- Case UI không hợp lệ kiểm 3 điều: có thông báo lỗi (hộp lỗi đỏ, hoặc theo A16: không gửi request và ô liên quan có `validationMessage` không rỗng), URL vẫn là `/register`, `GET /api/admin/users` không có thêm user.
- Case trùng email kiểm "vẫn chỉ có 1 user `test@eshop.com`".
- Case API: HTTP 4xx kèm trường `error` (A11).
- Email dùng hậu tố `{ts}` để không trùng giữa các lần chạy. Cleanup chung: xoá user bằng `DELETE /api/admin/users/:id` hoặc khởi động lại backend.

**TS-GUI (TC-FR01-90…94), step-by-step, technique `checklist`:**
- 90: ký hiệu `*` (FR-22.1)
- 91: `type="email"` (FR-22.2)
- 92: `type="password"` (FR-22.3)
- 93: thông báo lỗi nằm trên nút "Đăng Ký", đo bằng boundingBox (FR-22.4)
- 94 (thêm ngoài khối lệnh): case kiểm ô Xác nhận mật khẩu có tồn tại không (FR-01.9). A17 nhắc tới case này nhưng chưa có, nên em đặt vào suite này.

Thêm **A18**: ô Xác nhận mật khẩu cũng phải là `type="password"`, vì FR-22.3 chỉ nói "Trường Mật khẩu".

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: /domain-bva-testing HW02/A_FR01 3: TS-DOM (minimum set) + TS-GUI
- File đã tạo/sửa: HW02/A_FR01/testcases.json (suites TS-DOM 53 case, TS-GUI 5 case; giả định A18) · testcases.md (render) · ai-outputs/A_FR01_step3_20261019-1656.{json,md} + INDEX.md
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (V4 chưa có BVA → bước 4), 50/50 EC đã phủ · lint 0 lỗi / 1 cảnh báo (TS-DOM > 25 dòng) · test Not run
- Commit: chưa commit (chờ SV review) → dự kiến "HW02[A-FR01] 3/7: Test case Domain"
- Cần quyết định / câu hỏi:
  1. A17 hiểu theo chữ: thủ tục UI có bước nhập V5 → nếu thiếu ô Xác nhận mật khẩu thì cả 25 case UI (01–25) đều Blocked, không riêng 23–25. Có muốn: V5 = Mật khẩu (EC39) thì bỏ qua bước nhập, chỉ 23–25 Blocked không?
  2. TS-DOM 53 case (lint cảnh báo > 25 dòng): giữ một suite hay tách TS-DOM-UI / TS-DOM-API? Hoặc cắt bớt bản API của các lớp tách theo cơ chế HTML5 (EC4, EC14, EC24)?
  3. TC-02/TC-27 gom 4 lớp hợp lệ tách riêng (EC2, EC8, EC19, EC34) cho đúng minimum set → nếu Fail phải chạy tách lớp mới biết nguyên nhân. Chấp nhận không?
  4. TC-03 hoặc TC-FR01-14 khi chọn TC-FR01-14 (EC24, Mật khẩu rỗng): Xác nhận mật khẩu cũng để rỗng (= Mật khẩu), đã ghi trong notes. Kiểu gì V5 cũng bị vi phạm theo A7 → xác nhận cách xử lý này.
  5. TC-02 và TC-27 cùng tạo user 'Test@eshop.com' → hai case phải dọn dữ liệu (cleanup) giữa hai lần chạy, nếu không case thứ hai sẽ gặp trùng. Có đổi email cho một case không?
  6. Thêm TC-FR01-94 (kiểm sự tồn tại của ô Xác nhận mật khẩu, FR-01.9) vào TS-GUI, ngoài phạm vi khối lệnh → giữ hay chuyển chỗ?
  7. Ô có giá trị rỗng hoặc toàn khoảng trắng (TC-03/04/05/13/23…) trong bảng .md nhìn như ô trống → có cần render_md hiển thị dạng '' hoặc '␣␣␣' không?
```
````
*File AI ghi/gửi trong lượt này:* `fr01_step3_gen.py`

**Xử lý:** [...]

---

## #21 | 17:09 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
Commit riêng trước: "HW02: vá harness (render_md hiển thị chuỗi rỗng/khoảng trắng)" chỉ gồm .claude/skills/domain-bva-testing/scripts/render_md.py.

Sau đó áp dụng review bước 3 cho HW02/A_FR01 (em sửa trên bản đóng băng, KHÔNG freeze lại):
1. Tách TS-DOM thành TS-DOM-UI (TC-FR01-01…) và TS-DOM-API (đánh số tiếp), mỗi suite một procedure riêng. Ghi notes cho suite nào vẫn > 25 dòng: "giữ đủ lớp theo quy tắc mỗi case không hợp lệ phủ một lớp".
2. Case hợp lệ gộp: chỉ gộp lớp có căn cứ SRS (EC1/EC2, EC7, EC18, EC22, EC25, EC28, EC31, EC33/EC34, EC39). EC8 và EC19 (dựa trên giả định A3) mỗi lớp một case hợp lệ riêng, ở cả UI và API.
3. Case API của EC19 dùng biến thể hoa/thường khác với case UI (ví dụ 'TEST@eshop.com' so với 'Test@eshop.com') để hai case không phụ thuộc nhau.
4. A17 sửa thành: nếu thiếu ô Xác nhận mật khẩu, case có V5 = EC39 bỏ qua bước nhập V5 (ghi notes), chỉ các case EC40–EC42 → Blocked. Cập nhật procedure của TS-DOM-UI cho khớp.
5. TC của EC24 (Mật khẩu rỗng): thêm notes "V5 = V4 = rỗng; EC39/EC40 trùng nhau chỉ vì V4 rỗng; lỗi quy cho EC24 — đối chiếu validationMessage của ô Mật khẩu khi chạy".
6. Không đổi số TS-BVA (60–) và TS-GUI (90–).
7. Chạy check_domain (0 lỗi, 50/50 EC), lint, render. Commit "HW02[A-FR01] 3/7: Test case Domain" gồm testcases.json/.md, file đóng băng bước 3 + INDEX.md, A_prompt_log.md.
Báo cáo cho phiên thảo luận (kèm số TC mỗi suite).
8. Oracle tương đối: mọi Expected dạng "vẫn chỉ có đúng 1 user email 'test@eshop.com'" hoặc "không có thêm user nào" đổi thành "so với danh sách lấy ở bước 1 của chính case: không có user mới; user seed không bị sửa". Case hợp lệ: "đúng 1 user mới so với bước 1, có name/email như cột dữ liệu".
9. Cleanup hai tầng, ghi vào preconditions/cleanup của cả TS-DOM-UI và TS-DOM-API: (a) trước mỗi lượt chạy cả suite: khởi động lại backend để CSDL seed sạch; (b) sau mỗi case, kể cả khi Fail: xoá mọi user mới so với bước 1 bằng DELETE /api/admin/users/:id. Nếu xoá thất bại thì ghi notes, không đổi verdict của case.
10. Ghi giả định A19: "Tính độc lập giữa các case dựa trên dữ liệu riêng ({ts}) và oracle tương đối; cleanup là lớp bảo vệ thứ hai, vì API xoá user (FR-19) nằm ngoài phạm vi và có thể có lỗi."
11. Preconditions của TS-DOM-UI ghi đủ trạng thái ban đầu: trang /register vừa tải xong, cả 4 ô (Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu nếu có) đều trống; chưa đăng nhập (localStorage không có token); chạy tay thì dùng cửa sổ ẩn danh/tắt autofill; Playwright dùng browser context mới cho mỗi case.
12. Procedure của TS-DOM-UI viết rõ từng bước, mỗi bước có phản hồi quan sát được: (1) mở /register → 4 ô trống; (2) nhập lần lượt Họ Tên → Email → Mật khẩu → Xác nhận mật khẩu bằng cách gõ đúng chuỗi trong cột; ô có giá trị `''` (rỗng) thì không nhập gì, giữ nguyên ô trống; giá trị có ␣ thì gõ đúng số dấu cách đó → ô hiển thị đúng giá trị đã gõ (mật khẩu hiện dạng che); (3) bấm nút 'Đăng Ký' đúng một lần → hệ thống phản hồi; (4) quan sát: hộp lỗi đỏ trên form / bong bóng kiểm tra của trình duyệt / URL trên thanh địa chỉ → so với cột Expected; (5) kiểm CSDL theo oracle tương đối.
13. Procedure của TS-DOM-API ghi rõ: header Content-Type: application/json; khoá body name/email/password lấy từ cột dữ liệu; '— thiếu trường —' = bỏ khoá khỏi body; 'số …' = giá trị số JSON; '' = chuỗi rỗng; gửi đúng một request; quan sát HTTP status + body.
</pasted_content id="1f5a">
```

**Output:**
````
Đã commit `31f42ad`. Giờ dựng lại TS-DOM thành 2 suite UI và API; TS-GUI giữ nguyên.

Đã áp dụng đủ 13 mục review bước 3 và commit `448b10d`. Bản vá `render_md.py` commit riêng trước ở `31f42ad`. check_domain 0 lỗi, phủ 50/50 EC; lint 0 lỗi.

| Suite | Số TC | Mã | Nội dung |
|---|---|---|---|
| TS-DOM-UI | 27 | 01–27 | 2 case hợp lệ gộp (chỉ gồm lớp có căn cứ SRS) + EC8 riêng (03) + EC19 `Test@eshop.com` (04) + 20 case không hợp lệ (05–24) + 3 case V5 (25–27) |
| TS-DOM-API | 30 | 28–57 | 2 case hợp lệ gộp + EC8 (30) + EC19 `TEST@eshop.com` (31) + 20 case không hợp lệ (32–51) + 6 lớp chỉ có ở API (52–57) |
| TS-GUI | 5 | 90–94 | không đổi |
| **Tổng** | **62** | | TS-BVA vẫn để trống từ 60 |

**Thay đổi chính:**
- **Oracle tương đối:** không còn chỗ nào ghi "vẫn chỉ có đúng 1…" hay "không có thêm user".
- **Hai suite tách theo tầng:** mỗi suite có procedure, preconditions và cleanup riêng theo mục 9, 11, 12, 13. Cả hai đều có notes "giữ đủ lớp…" vì vẫn hơn 25 dòng.
- **A17 sửa** theo mục 4; thêm **A19**. TC-FR01-17 (EC24) có notes theo mục 5. Các case V5 = EC39 có notes "bỏ qua bước nhập V5 nếu thiếu ô".
- **Bỏ cột thừa:** cột "Tầng" không cần nữa vì đã tách suite; TS-DOM-API không có cột Xác nhận mật khẩu (A8).

**Lệch so với khối lệnh:** mục 12 đánh số bước "mở `/register`" là (1). Nhưng oracle mục 8 so với "danh sách lấy ở bước 1", nên em đặt bước lấy danh sách user (`GET /api/admin/users`) làm bước 1. Năm bước của mục 12 thành bước 2–6 (API: 2–4).

**Chỗ `render_md.py` chưa hiển thị** (dữ liệu trong JSON vẫn đủ):
- Các bước của TS-GUI không có trong `.md`, chỉ có bảng tóm tắt.
- `notes` của suite không hiện.
- Tiêu đề "Bước 3b — Minimum Set" chỉ nhận mã `TS-DOM`, nên hai suite mới hiện tên mặc định.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: vá render_md (commit riêng) + áp dụng review bước 3 HW02/A_FR01 (không freeze lại) + commit 3/7
- File đã tạo/sửa:
  - .claude/skills/domain-bva-testing/scripts/render_md.py (commit riêng)
  - HW02/A_FR01/testcases.json:
    - tách TS-DOM-UI 27 TC (01–27) / TS-DOM-API 30 TC (28–57), TS-GUI 5 TC (90–94) giữ nguyên → tổng 62
    - EC8, EC19 có case hợp lệ riêng ở cả hai tầng; EC19: UI 'Test@eshop.com', API 'TEST@eshop.com'
    - oracle tương đối; preconditions/procedure/cleanup hai tầng
    - A17 sửa, thêm A19
  - testcases.md (render lại)
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (V4 chưa có BVA → bước 4), 50/50 EC · lint 0 lỗi / 2 cảnh báo (hai suite > 25 dòng, đã ghi notes) · test Not run
- Commit:
  - 31f42ad HW02: vá harness (render_md hiển thị chuỗi rỗng/khoảng trắng)
  - 448b10d HW02[A-FR01] 3/7: Test case Domain (testcases.json/.md, A_FR01_step3_20261019-1656.{json,md}, INDEX.md, A_prompt_log.md)
- Cần quyết định / câu hỏi:
  1. Procedure: bước lấy danh sách user là bước 1 (để oracle "bước 1" đúng), 5 bước của mục 12 thành bước 2–6. Đồng ý không?
  2. render_md chưa hiển thị: các bước của suite step-by-step (TS-GUI), notes của suite, tiêu đề "Bước 3b" cho TS-DOM-UI/API → vá harness thêm một commit riêng không?
  3. Bước tiếp theo: /domain-bva-testing HW02/A_FR01 4 (TS-BVA từ TC-FR01-60; với 2 tầng UI/API, dải 60–89 chỉ có 30 mã).
```
````
*File AI ghi/gửi trong lượt này:* `fr01_step3_split.py`

**Xử lý:** [...]

---

## #22 | 17:17 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
(a) Commit riêng "HW02: vá harness (SKILL.md: quy tắc tiền điều kiện/cách nhập; render_md: bước chi tiết, ghi chú suite, tiêu đề suite)" gồm .claude/skills/domain-bva-testing/SKILL.md và scripts/render_md.py.
(b) Render lại HW02/A_FR01/testcases.md, kiểm TS-GUI đã hiện bước chi tiết. Commit "HW02[A-FR01] 3/7: render lại (bước chi tiết TS-GUI, ghi chú suite)" gồm testcases.md, A_prompt_log.md.
(c) Ghi vào CLAUDE.md mục "Quyết định đã chốt": dải mã TC — TS-DOM 01–59, TS-BVA 60–89 (tràn thì từ 100), TS-GUI 90–99, TS-SV (SV bổ sung) từ 200. Gộp vào commit (a).
(d) Chạy: /domain-bva-testing HW02/A_FR01 4
    Ràng buộc: mô hình 9 điểm theo slide; bước nhảy 1 ký tự; biến đang xét chạy qua điểm biên, các biến khác giữ nominal hợp lệ; ghi "layer" UI/API cho từng case; MIN_UI/MAX_UI chỉ thêm khi giao diện thật sự giới hạn (maxlength…) — không có thì ghi lý do vào notes; dùng lại preconditions/procedure/cleanup của TS-DOM-UI/API. Chạy freeze --step 4, check_domain, lint, render. KHÔNG commit. Dừng hẳn sau bước này.
Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Thêm quyết định dải mã TC vào CLAUDE.md, commit (a), render lại và commit (b).

TS-GUI giờ đã hiện đủ bước chi tiết. Commit (b).

Giờ đến bước 4. Đọc lại SKILL.md (đã sửa) và kiểm UI có `maxlength` không.

Xong cả bốn phần (a)–(d). Bước 4 có 38 case BVA. check_domain 0 lỗi, phủ 50/50 EC; lint 0 lỗi. Bản nháp bước 4 đã freeze, chưa commit. Em dừng ở đây; bước 5 là phần của em.

**(a)–(c):** commit harness `1816c8a` (SKILL.md, render_md.py, dòng dải mã TC trong CLAUDE.md). Render lại và commit `1e5f539`: TS-GUI giờ hiện đủ bước, tiền điều kiện, dữ liệu, dọn dẹp; tiêu đề suite và ghi chú suite cũng đã hiện.

**(d) Bước 4.** Tách thành hai suite theo tầng, giống TS-DOM:

| Suite | Số TC | Mã |
|---|---|---|
| TS-BVA-UI | 19 | 60–78 |
| TS-BVA-API | 19 | 79–89 rồi 100–107 (tràn theo quyết định dải mã) |

Mỗi tầng xét 6 chiều. Các chiều này có thứ tự theo SRS; mọi biến khác giữ giá trị danh nghĩa.

| Chiều | Điểm | Giá trị |
|---|---|---|
| Độ dài Họ Tên (≥ 1) | LB-1 / LB / LB+1 | `''` / `A` / `An` |
| Độ dài Mật khẩu (≥ 8) | LB-1 / LB / LB+1 / NOM | 7 / 8 / 9 / 12 ký tự |
| Số chữ hoa (≥ 1) | 0 / 1 / 2 | `abcd1234!` / `Abcd1234!` / `ABcd1234!` |
| Số chữ thường (≥ 1) | 0 / 1 / 2 | `ABCD1234!` / `ABCd1234!` / `ABCde123!` |
| Số chữ số (≥ 1) | 0 / 1 / 2 | `Abcdefgh!` / `Abcdefg1!` / `Abcdef12!` |
| Số ký tự đặc biệt (≥ 1) | 0 / 1 / 2 | `Abcd12345` / `Abcd1234@` / `Abcd123!@` |

- **Không có UB-1/UB/UB+1:** SRS không có cận trên (A1, A4). check_domain còn đúng 1 cảnh báo về chuyện này, đã giải thích trong notes của suite.
- **Không có MIN_UI/MAX_UI:** Register.jsx dòng 37–63 không có `maxlength`/`minlength`. Lý do ghi trong notes.
- **Email không có điểm biên:** SRS chỉ quy định định dạng (A2).
- **Dùng lại từ TS-DOM:** preconditions, procedure, cleanup và oracle tương đối.
- **Dữ liệu trùng:** các điểm LB-1 trùng dữ liệu với case EC3/23/26/29/32/35 của TS-DOM. Em giữ lại để bảng BVA đủ điểm, rationale có ghi rõ.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: (a) vá harness + quyết định dải mã · (b) render lại bước 3 · (d) /domain-bva-testing HW02/A_FR01 4
- File đã tạo/sửa:
  - (a) .claude/skills/domain-bva-testing/SKILL.md, scripts/render_md.py, CLAUDE.md (dải mã TC)
  - (b) HW02/A_FR01/testcases.md
  - (d) testcases.json (thêm TS-BVA-UI 19 TC: 60–78; TS-BVA-API 19 TC: 79–89 + 100–107; các phần khác không đổi, diff chỉ có dòng thêm) · testcases.md · ai-outputs/A_FR01_step4_20261019-1719.{json,md} + INDEX.md
- Số TC mỗi suite: TS-DOM-UI 27 · TS-DOM-API 30 · TS-BVA-UI 19 · TS-BVA-API 19 · TS-GUI 5 → tổng 100 (AI 100, Not run 100)
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (thiếu UB do A4, đã ghi lý do) · 50/50 EC · lint 0 lỗi / 2 cảnh báo (TS-DOM > 25 dòng, đã ghi notes) · test Not run
- Commit: 1816c8a HW02: vá harness (SKILL.md…; render_md…) · 1e5f539 HW02[A-FR01] 3/7: render lại (bước chi tiết TS-GUI, ghi chú suite) · bước 4: chưa commit (chờ SV review) → dự kiến "HW02[A-FR01] 4/7: Test case BVA"
- Cần quyết định / câu hỏi:
  1. BVA cho số ký tự mỗi loại (count ≥ 1) có được tính là "lớp có thứ tự" không? Nếu bỏ thì còn 7 điểm/tầng (14 TC).
  2. Điểm LB-1 trùng dữ liệu với case TS-DOM: giữ (bảng BVA đủ điểm) hay thay bằng tham chiếu tới TC của TS-DOM?
  3. Mã TS-BVA-API tràn sang 100–107 theo quy tắc; nếu muốn liền mạch thì chỉ giữ BVA tầng API cho độ dài Mật khẩu.
  4. Trường mới "bva_dimension" (chiều đang xét) không có trong schema của test-case-writing; render_md chưa hiện trường này (tên chiều đã ghi trong tiêu đề case).
  5. A_prompt_log.md sẽ được hook tạo lại sau lượt này → đưa vào commit 4/7.
```
````
*File AI ghi/gửi trong lượt này:* `fr01_step4_bva.py`

**Xử lý:** [...]

---

## #23 | 17:25 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
Áp dụng review bước 4 cho HW02/A_FR01 (KHÔNG freeze lại):
- Với mỗi case LB-1 của TS-BVA-UI/API có dữ liệu trùng case TS-DOM, thêm notes: "Cùng giá trị với <mã TC TS-DOM>: điểm này vừa là đại diện lớp vừa là LB-1; giữ để bảng BVA đủ điểm theo slide."
- Chạy check_domain, lint, render.
- Commit "HW02[A-FR01] 4/7: Test case BVA" gồm testcases.json/.md, A_FR01_step4_20261019-1719.{json,md}, INDEX.md, A_prompt_log.md.
Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Em đã thêm notes cho 12 case LB-1 trùng dữ liệu với TS-DOM và commit bước 4 ở `b567dc2`. Không freeze lại.

Mã TS-DOM được ghép theo cùng tầng, cùng lớp EC và cùng dữ liệu nhập (chỉ khác Email). Các case UI đã có sẵn note "bỏ qua V5 (A17)"; câu mới nối vào sau.

| Lớp | TS-BVA-UI → TS-DOM-UI | TS-BVA-API → TS-DOM-API |
|---|---|---|
| EC3 (Họ Tên 0 ký tự) | 60 → 05 | 79 → 32 |
| EC23 (Mật khẩu 7 ký tự) | 63 → 16 | 82 → 43 |
| EC26 (0 chữ hoa) | 67 → 18 | 86 → 45 |
| EC29 (0 chữ thường) | 70 → 20 | 89 → 47 |
| EC32 (0 chữ số) | 73 → 22 | 102 → 49 |
| EC35 (0 ký tự đặc biệt) | 76 → 23 | 105 → 50 |

Phần thiết kế của AI (bước 1–4) đã xong. Bước 5 là phần em tự làm: thêm suite TS-SV, mã từ 200. Theo quy tắc mục 3, em không gợi ý thêm case cho tới khi em hỏi phần gap analysis.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: áp dụng review bước 4 HW02/A_FR01 (không freeze lại) + commit 4/7
- File đã tạo/sửa: HW02/A_FR01/testcases.json (notes cho 12 case LB-1: TC-FR01-60, 63, 67, 70, 73, 76, 79, 82, 86, 89, 102, 105) · testcases.md (render lại)
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (thiếu UB do A4) · 50/50 EC · lint 0 lỗi / 2 cảnh báo (TS-DOM-UI/API > 25 dòng, đã ghi notes) · test Not run · tổng 100 TC (DOM-UI 27, DOM-API 30, BVA-UI 19, BVA-API 19, GUI 5)
- Commit: b567dc2 HW02[A-FR01] 4/7: Test case BVA (testcases.json/.md, A_FR01_step4_20261019-1719.{json,md}, INDEX.md, A_prompt_log.md)
- Cần quyết định / câu hỏi:
  1. Bước 5 do SV làm 🔒: SV tự thêm TS-SV (TC-FR01-200…, origin Human), chạy check_domain rồi mới hỏi AI "vì sao bỏ sót"; so sánh với bản đóng băng bước 3 (A_FR01_step3_20261019-1656) và bước 4 (A_FR01_step4_20261019-1719).
  2. A_prompt_log.md trong commit chưa có lượt này (hook chạy sau khi lượt kết thúc) → đưa vào commit 5/7.
```
````

**Xử lý:** [...]

---

## #24 | 17:45 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
Sửa HW02/A_FR01/testcases.json theo review của SV (KHÔNG freeze, đây là chỉnh sửa của SV):
- TC-FR01-90: expected → "3 nhãn Họ Tên, Email, Mật khẩu (các trường bắt buộc FR-01 liệt kê) đều có ký hiệu '*' (FR-22.1)." Nếu form có ô Xác nhận mật khẩu thì ghi nhận thêm có '*' hay không nhưng không dùng để kết luận case này.
- TC-FR01-92: chỉ kiểm ô Mật khẩu có type="password" và che ký tự. Phần ô Xác nhận mật khẩu: ghi notes "kiểm khi ô tồn tại; sự tồn tại do TC-FR01-94 kết luận (A17)".
- Cả hai: origin "Both", notes ghi lý do sửa: "SV sửa: tránh một nguyên nhân (thiếu ô Xác nhận mật khẩu) làm fail nhiều case; FR-01 chỉ liệt kê 3 trường bắt buộc."
- Rà các case khác xem còn case nào có expected phụ thuộc vào việc ô Xác nhận mật khẩu tồn tại mà không thuộc nhóm A17 (EC39–42, TC-94) không. Chỉ liệt kê, không tự sửa.
- Chạy check_domain, lint, render.
- Nếu commit 4/7 chưa tạo: gộp vào 4/7. Nếu đã tạo: commit riêng "HW02[A-FR01] 4/7b: SV sửa TC-90, TC-92 cô lập nguyên nhân thiếu ô Xác nhận mật khẩu" (kèm A_prompt_log.md).
Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Đã rà xong. Giờ sửa TC-90 và TC-92: tiêu đề, bước và dữ liệu đổi theo expected mới cho nhất quán.

Commit 4/7 đã tạo trước đó (`b567dc2`), nên làm commit riêng 4/7b.

Em đã sửa TC-90 và TC-92 theo review và commit riêng ở `6a5a17e` (commit 4/7 đã có từ trước). Không freeze lại. check_domain và lint đều 0 lỗi.

**Đã sửa:**
- **TC-FR01-90:** expected còn 3 nhãn Họ Tên, Email, Mật khẩu. Em sửa cả bước 2, test_data và rationale để khớp. Ô Xác nhận mật khẩu, nếu có, chỉ ghi nhận có `*` hay không, không dùng để kết luận case.
- **TC-FR01-92:** chỉ kiểm ô Mật khẩu. Em bỏ bước 4 (kiểm type ô Xác nhận mật khẩu), đổi tiêu đề và rationale; phần ô Xác nhận chuyển vào notes đúng câu em đưa.
- **Cả hai case:** origin `Both`, notes có lý do sửa. Diff chỉ nằm trong hai case này.

**Rà các case khác.** Các chỗ dưới đây vẫn phụ thuộc vào việc ô Xác nhận mật khẩu tồn tại mà không thuộc nhóm A17. Em chưa sửa:
1. **TC-FR01-93 bước 2:** gõ "Xác nhận mật khẩu 'abcd1234!'" nhưng không có hướng dẫn bỏ qua khi thiếu ô. Nếu thiếu ô thì case này hỏng ở bước nhập, chưa tới chỗ đo vị trí thông báo lỗi (FR-22.4).
2. **Procedure bước 3 của TS-DOM-UI và TS-BVA-UI:** cột expected ghi "Mật khẩu và Xác nhận mật khẩu hiện dạng che". Phần action đã có nhánh A17 nhưng expected không ghi "(nếu có)", khác với bước 2 đã ghi.
3. **A18:** vẫn ghi "kiểm ở TC-FR01-92", nhưng TC-92 không còn kiểm ô Xác nhận mật khẩu, nên A18 hiện không có case nào kiểm.

TC-25/26/27 (EC40–EC42) và TC-94 thuộc nhóm A17, không cần đổi.

Có file `HW02/A_FR01/sv_cases.md` chưa được git theo dõi. Em không mở và không đưa vào commit.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: SV sửa TC-FR01-90, TC-FR01-92 (không freeze) + rà các case phụ thuộc ô Xác nhận mật khẩu
- File đã tạo/sửa: HW02/A_FR01/testcases.json (TC-90: steps[1], test_data, expected, rationale, origin Both, notes · TC-92: title, bỏ bước 4, expected, rationale, origin Both, notes) · testcases.md (render)
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (thiếu UB do A4) · origin AI 98, Both 2 · lint 0 lỗi / 2 cảnh báo (TS-DOM > 25 dòng) · test Not run
- Commit: 6a5a17e HW02[A-FR01] 4/7b: SV sửa TC-90, TC-92 cô lập nguyên nhân thiếu ô Xác nhận mật khẩu (testcases.json/.md, A_prompt_log.md)
- Cần quyết định / câu hỏi (chỉ liệt kê, chưa sửa):
  1. TC-FR01-93 bước 2 nhập Xác nhận mật khẩu, không có nhánh A17 → thiếu ô thì case FR-22.4 hỏng ở bước nhập.
  2. Procedure bước 3 của TS-DOM-UI và TS-BVA-UI: expected "Mật khẩu và Xác nhận mật khẩu hiện dạng che" chưa ghi "(nếu có)".
  3. A18 vẫn tham chiếu TC-FR01-92, nhưng TC-92 không còn kiểm ô Xác nhận mật khẩu → sửa A18 hoặc gán case khác.
  4. HW02/A_FR01/sv_cases.md chưa được git theo dõi (AI không mở) → SV tự xử lý ở bước 5.
```
````

**Xử lý:** [...]

---

## #25 | 19:14 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
   Chép các case trong HW02/A_FR01/sv_cases.md vào suite TS-SV (mã từ TC-FR01-200, origin "Human"), giữ nguyên ý của em, chỉ chuẩn hoá theo schema (tiêu đề Action+Function+Condition, covers nếu khớp EC có sẵn, nếu không khớp EC nào thì ghi rõ "lớp mới"). Không thêm, bớt hay sửa expected.
   Sau đó, với TỪNG case của em, đối chiếu với các bản đóng băng bước 2–4 trong appendix/ai-outputs/ và trả lời trung thực:
   (a) case này đã có trong bản nháp của AI chưa (ghi mã EC/TC nếu có);
   (b) nếu chưa: AI đã nghĩ tới nhưng không đưa vào output, hay không nghĩ tới;
   (c) nguyên nhân thuộc loại nào: thông tin trong prompt chưa đủ, giới hạn của công cụ, hay độ phức tạp của feature — kèm 1–2 câu giải thích.
   Không đề xuất thêm case mới. Chạy check_domain, render. Commit "HW02[A-FR01] 5/7: đưa case SV vào TS-SV + câu trả lời gap analysis của AI".
   Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Đã lấy được bảng EC → TC từ bản đóng băng bước 4. Giờ viết suite TS-SV.

Lint báo TC-200 và TC-201 trùng dữ liệu, vì hai case chỉ khác tầng mà tầng chưa có trong cột. Em thêm cột "Tầng" vào TS-SV rồi sinh lại.

Đã chép 24 case vào TS-SV (TC-FR01-200…223). Giờ viết câu trả lời gap analysis vào file riêng, ghi rõ đó là lời của AI.

Em đã chép 24 case của em vào suite TS-SV (TC-FR01-200 đến 223, origin `Human`), trả lời gap analysis cho từng case và commit ở `8d837f1`. check_domain 0 lỗi; lint 0 lỗi.

**Cách chuẩn hoá TS-SV:**
- Expected, Lý do (vào `rationale`) và Actual (vào `actual_result`) chép nguyên văn. Status để `Not run`, vì nhiều dòng có hai verdict khác nhau cho UI và API.
- Thêm cột "Tầng" vì lint báo SV-01 và SV-02 trùng dữ liệu khi chưa phân biệt tầng. Thêm cột "Thao tác riêng", tách từ phần Lý do/Expected của em (bấm 2 lần, gửi đồng thời, `{}`, `text/plain`, thêm `role`, đăng nhập sau khi đăng ký…).
- Layer `UI+API` cho các dòng em ghi cả hai tầng. Giá trị này ngoài schema (chỉ có UI/API/Mobile).
- 16 case khớp EC có sẵn. 7 case ghi "lớp mới": SV-04, 05, 09, 10, 15, 22, 23, 24.
- SV-14 (`{}`) vi phạm cùng lúc EC5, EC16 và EC37. Em ghi là "lớp mới: tổ hợp", vì ghi cả ba mã thì check_domain báo lỗi; notes đã giải thích.
- 4 case chưa gán mã yêu cầu vì em không ghi mã cụ thể: SV-08 ("FR-01" chung), SV-15, SV-23, SV-24. Lint báo 4 cảnh báo cho chỗ này.

**Câu trả lời gap analysis** nằm trong `HW02/A_FR01/ai_gap_answer.md`, ghi rõ là lời của AI, không phải phân tích của SV. Mỗi case có (a), (b), (c), mã EC/TC lấy theo bản đóng băng bước 4.

Vài điểm em nên tự kiểm khi viết phần phân tích:
- **Đã nghĩ tới nhưng không đưa vào:**
  - SV-04/05: chính AI viết luật "không rỗng hai bên dấu chấm" trong A2 nhưng không tách lớp.
  - SV-03: mô tả EC36 có ghi khoảng trắng nhưng AI chọn `#`.
  - SV-08: A12 có nhắc đăng nhập.
  - SV-13: AI có grep `limit` trong server.js.
  - SV-14: AI bỏ tổ hợp có chủ đích theo quy tắc mỗi case một lớp.
  - SV-16: AI đã đọc SEC-05.
  - SV-07 (một phần): bản nháp A3 bước 1 đề xuất không phân biệt hoa/thường, nhưng không tách phần local và domain.
- **SV-01:** AI đã đọc regex ở Register.jsx dòng 15 từ bước 0 nhưng không kiểm mật khẩu danh nghĩa `Abcd1234!` của chính mình có qua được phía client không.
- **SV-02** không phải bỏ sót, chỉ khác giá trị đại diện.

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: bước 5 HW02/A_FR01: chép case SV vào TS-SV + câu trả lời gap analysis của AI
- File đã tạo/sửa: HW02/A_FR01/testcases.json (thêm TS-SV 24 TC: TC-FR01-200…223) · testcases.md (render) · HW02/A_FR01/ai_gap_answer.md (mới, câu trả lời của AI)
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (UB do A4), 50/50 EC · lint 0 lỗi / 6 cảnh báo (4 case SV chưa gán mã yêu cầu; 2 suite TS-DOM > 25 dòng) · tổng 124 TC (AI 98, Both 2, Human 24) · test: tất cả Not run trong JSON (Actual SV ghi tay đã chép vào actual_result)
- Commit: 8d837f1 HW02[A-FR01] 5/7: đưa case SV vào TS-SV + câu trả lời gap analysis của AI (sv_cases.md đã có từ commit 2448cf1)
- Cần quyết định / câu hỏi:
  1. Status của TS-SV: để Not run chờ bước 6, hay SV chốt verdict theo từng tầng? Với dòng UI+API có hai verdict, có tách thành hai case không? (Hiện giữ 1:1 theo sv_cases.md.)
  2. layer "UI+API" không có trong schema (UI/API/Mobile) → giữ hay tách?
  3. SV-07 có Expected ngược với A3/EC19 → cần chốt lại A3 (domain không phân biệt hoa/thường?) trước bước 6.
  4. SV-08, SV-15, SV-23, SV-24 chưa gán mã yêu cầu → SV chọn mã hoặc ghi "ngoài FR-01".
  5. ai_gap_answer.md là lời của AI → khai trong Audit/Disclosure; phần "vì sao AI bỏ sót" trong report do SV tự viết.
```
````
*File AI ghi/gửi trong lượt này:* `fr01_step5_sv.py`, `ai_gap_answer.md`

**Xử lý:** [...]

---

## #26 | 19:28 19/10/2026 | Claude Opus 5.5 | [...]
**Mục đích:** [...]

**Prompt:**
```
<pasted_content id="1f5a">
A. Vá harness (commit riêng "HW02: vá harness – render_md chỉ đánh dấu rỗng cho biến đầu vào"):
   render_md.py suite_table: chỉ áp show() (hiện `''` (rỗng)/␣) cho cột là biến đầu vào trong domain.variables; cột khác để trống nếu không có giá trị.

B. Sửa TS-SV trong HW02/A_FR01/testcases.json theo quyết định của SV (KHÔNG freeze):
   1. Chuyển Actual ghi tay từ actual_result (và câu "Actual: …" trong rationale của TC-200) sang notes: "Quan sát thăm dò (SV chạy tay 19/10): …". actual_result rỗng, status Not run.
   2. Tách 10 dòng UI+API (202–205, 210, 211, 215, 217, 218 → UI giữ mã; API mã mới từ TC-FR01-224 theo thứ tự). TC-216 layer UI. Origin Human, notes "tách từ TC-xxx". Không đổi dữ liệu/expected.
   3. Thêm vào preconditions của TS-SV: trạng thái ban đầu các case UI như TS-DOM-UI (trang /register vừa tải, các ô trống, chưa đăng nhập, không autofill), trừ TC-223.
   4. Thêm meta.assumptions A20 đúng nguyên văn SV sẽ gửi (CHỜ — không tự viết).
   5. Mục A3, mã yêu cầu cho 207/214/222/223, oracle cho 219/223: CHỜ SV gửi quyết định, chưa sửa.
   Chạy check_domain, lint, render. Chưa commit — báo cáo danh sách mã mới và các mục đang chờ.
Báo cáo cho phiên thảo luận.
</pasted_content id="1f5a">
```

**Output:**
````
Bản vá render đã commit ở `85458ad`. Giờ sửa TS-SV: chuyển phần quan sát sang notes, tách các dòng UI+API, thêm tiền điều kiện.

Bản vá render đã commit ở `85458ad`. Phần B đã sửa xong trong `testcases.json`, chưa commit; mục 4 và 5 đang chờ quyết định của em. check_domain 0 lỗi, 50/50 EC; lint 0 lỗi.

**A. render_md.py:** `show()` giờ chỉ áp cho cột trùng tên biến đầu vào: Họ Tên, Email, Mật khẩu, Xác nhận mật khẩu. Cột "Thao tác riêng" và "Tầng" khi trống thì để trống. Cột "Email trong CSDL" không trùng tên V3 nên cũng không áp, nhưng cột này không bao giờ rỗng.

**B1. Actual chuyển sang notes:** cả 24 case có notes "Quan sát thăm dò (SV chạy tay 19/10): …". `actual_result` rỗng hết, status `Not run`. Câu "Actual: …" trong rationale của TC-200 cũng đã chuyển sang notes.

**B2. Tách các dòng UI+API:** em đếm được 10 dòng UI+API. 9 dòng được tách; TC-216 chỉ đổi layer thành UI, không tách. Bản UI giữ mã cũ, bản API mang mã mới:

| UI (giữ mã) | 202 | 203 | 204 | 205 | 210 | 211 | 215 | 217 | 218 |
|---|---|---|---|---|---|---|---|---|---|
| API (mã mới) | 224 | 225 | 226 | 227 | 228 | 229 | 230 | 231 | 232 |

- Dữ liệu và expected không đổi.
- Tiêu đề đổi "qua UI và API" thành "qua UI" hoặc "qua API".
- Notes ghi hai chiều: bản API có "Tách từ TC-xxx"; bản UI có "Bản API tách thành TC-xxx".

**B3:** đã thêm tiền điều kiện trạng thái ban đầu cho các case tầng UI của TS-SV, trừ TC-223.

Có 3 chỗ em nên xem trước khi commit:
- Mỗi cặp tách ra đều mang nguyên câu quan sát gồm cả phần API lẫn UI, vì em không tự cắt câu của em. Muốn mỗi bản chỉ giữ phần của tầng mình thì em nói.
- Expected của TC-227 (bản API của SV-06) vẫn có "chuyển tới /login", vốn chỉ đúng ở UI. Em không sửa vì lệnh là không đổi expected.
- TS-SV giờ có 33 dòng, lint cảnh báo thêm "> 25 dòng" (tổng 7 cảnh báo).

```
### Báo cáo cho phiên thảo luận
- Nhiệm vụ: A. vá render_md (show() chỉ cho cột biến đầu vào) · B. sửa TS-SV theo quyết định SV (không freeze)
- File đã tạo/sửa:
  - .claude/skills/domain-bva-testing/scripts/render_md.py (đã commit)
  - HW02/A_FR01/testcases.json (TS-SV: chuyển Actual sang notes; tách 9 dòng; TC-216 → UI; thêm tiền điều kiện UI)
  - testcases.md (render)
- Mã mới (bản API): 202→224, 203→225, 204→226, 205→227, 210→228, 211→229, 215→230, 217→231, 218→232. TS-SV 33 TC; tổng 133 (AI 98, Both 2, Human 33)
- Kết quả kiểm tra: check_domain 0 lỗi / 1 cảnh báo (UB do A4), 50/50 EC · lint 0 lỗi / 7 cảnh báo (4 case chưa gán mã yêu cầu; TS-DOM-UI, TS-DOM-API, TS-SV > 25 dòng) · test Not run (133)
- Commit: 85458ad HW02: vá harness – render_md chỉ đánh dấu rỗng cho biến đầu vào · phần B chưa commit
- Đang chờ SV:
  1. A20: nguyên văn do SV gửi.
  2. A3: chốt lại trường hợp chỉ khác hoa/thường ở phần domain (SV-07, TC-206).
  3. Mã yêu cầu cho TC-207, 214, 222, 223.
  4. Oracle cho TC-219 (homoglyph) và TC-223 (đang đăng nhập).
- Cần quyết định / câu hỏi:
  5. Mỗi cặp tách ra đều mang nguyên câu quan sát (cả UI lẫn API) → giữ hay chỉ để phần của tầng tương ứng?
  6. Expected của TC-227 (SV-06 bản API) có "chuyển tới /login" → SV có sửa expected cho bản API không?
  7. Đề xuất message commit khi xong: "HW02[A-FR01] 5/7b: SV chuẩn hoá TS-SV (tách UI/API, quan sát sang notes)".
```
````

**Xử lý:** [...]

---

**Tổng:** 26 lượt; Claude Sonnet 4.6 3 lượt (#1, #2, #3); Claude Opus 5.5 24 lượt (#3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26). 1 lượt có output từ hơn một model nên được đếm ở cả hai.
