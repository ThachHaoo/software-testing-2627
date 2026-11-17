# HW04 – bug report

## Quyết định (SV chốt, lệnh #20)

- **G → BUG = Cách 2:** mỗi nhóm Fail (G) = 1 bug.
  - Lý do SV: bám `_groups` (`_groups_AB.md`, `_groups_C.md`); bước tái hiện gọn; confirmation test được từng hành vi.
  - **Quyết định giữ riêng BUG-88, BUG-91, BUG-94 (không gộp vào BUG-86 và BUG-89):** Dù cùng chung vị trí lỗi ở mã nguồn, hành vi người dùng quan sát được và bước kiểm thử khác nhau:
    - **BUG-88 (A-G3)** khác **BUG-86 (A-G1)** ở trường hợp đầu vào có khoảng trắng đầu chuỗi (` Hiep123$`) và kéo theo bước kiểm thử luồng đăng nhập lại sau khi đăng ký.
    - **BUG-91 (B-G3)** khác **BUG-89 (B-G1)** ở trạng thái người dùng đã đăng nhập và kiểm tra phản hồi trực quan tức thì trong ≤ 2 giây ngay sau thao tác bấm.
    - **BUG-94 (B-G6)** khác **BUG-89 (B-G1)** ở luồng thao tác thêm nhiều lần liên tiếp có điều hướng sang trang giỏ hàng ở giữa để kiểm tra logic cộng dồn số lượng.
- **B1 = b:** tạo issue **mới** trên `tkob-team/eshop-sut` cho mọi bug (không comment vào issue HW02). Tiêu đề GitHub: `[HW04][FR-xx] …`. Mục "Liên quan" của mỗi bug trỏ issue HW02.
- **Đánh số:** tiếp toàn môn — HW03 dừng ở BUG-85 (đã kiểm `HW03/bugs/`) → HW04 bắt đầu từ **BUG-86**.
- Khung `BUG-xx.md` theo mẫu HW02 (`HW02/bugs/BUG-22.md` @ d0d0e05). Ô `<SV viết>`: Tiêu đề, Severity, Priority, Tiền điều kiện, Bước tái hiện, Expected, Actual, Nhận định. AI chỉ điền dữ kiện (môi trường, TC, bằng chứng, yêu cầu theo HW02, assertion nguyên văn, code SUT, liên quan).

## Bảng G → BUG

| BUG | Feature | G | TC (Fail cả chrome/edge/firefox) | Issue HW02 liên quan | Issue HW04 |
|---|---|---|---|---|---|
| BUG-86 | A – FR-01 | A-G1 | TC-FR01-01, 02, 64, 68, 74, 77 | BUG-01 #17 | [#298](https://github.com/tkob-team/eshop-sut/issues/298) |
| BUG-87 | A – FR-01 | A-G2 | TC-FR01-202 | BUG-02 #18 | [#299](https://github.com/tkob-team/eshop-sut/issues/299) |
| BUG-88 | A – FR-01 | A-G3 | TC-FR01-211 | BUG-01 #17 | [#300](https://github.com/tkob-team/eshop-sut/issues/300) |
| BUG-89 | B – FR-07 | B-G1 | TC-FR07-61, 62, 63, 64 | BUG-15 #161 | [#301](https://github.com/tkob-team/eshop-sut/issues/301) |
| BUG-90 | B – FR-07 | B-G2 | TC-FR07-01 | BUG-21 #167 | [#302](https://github.com/tkob-team/eshop-sut/issues/302) |
| BUG-91 | B – FR-07 | B-G3 | TC-FR07-02 | BUG-15 #161 | [#303](https://github.com/tkob-team/eshop-sut/issues/303) |
| BUG-92 | B – FR-07 | B-G4 | TC-FR07-04 | BUG-20 #166; BUG-15 #161 | [#304](https://github.com/tkob-team/eshop-sut/issues/304) |
| BUG-93 | B – FR-07 | B-G5 | TC-FR07-08 | BUG-19 #165 | [#305](https://github.com/tkob-team/eshop-sut/issues/305) |
| BUG-94 | B – FR-07 | B-G6 | TC-FR07-205 | BUG-15 #161 | [#306](https://github.com/tkob-team/eshop-sut/issues/306) |
| BUG-95 | C – FR-15 | C-G1 | TC-FR15-03 | BUG-45 #191 | [#307](https://github.com/tkob-team/eshop-sut/issues/307) |
| BUG-96 | C – FR-15 | C-G2 | TC-FR15-10 | BUG-36 #182 | [#308](https://github.com/tkob-team/eshop-sut/issues/308) |
| BUG-97 | C – FR-15 | C-G3 | TC-FR15-11 | BUG-36 #182 | [#309](https://github.com/tkob-team/eshop-sut/issues/309) |
| BUG-98 | C – FR-15 | C-G4 | TC-FR15-15 | BUG-38 #184 (+ annotation BUG-48 #194) | [#310](https://github.com/tkob-team/eshop-sut/issues/310) |
| BUG-99 | C – FR-15 | C-G5 | TC-FR15-200 | BUG-39 #185 | [#311](https://github.com/tkob-team/eshop-sut/issues/311) |
| BUG-100 | C – FR-15 | C-G6 | TC-FR15-201 | BUG-40 #186 | [#312](https://github.com/tkob-team/eshop-sut/issues/312) |
| BUG-101 | C – FR-15 | C-G7 | TC-FR15-66 | BUG-35 #181 | [#313](https://github.com/tkob-team/eshop-sut/issues/313) |
| BUG-102 | C – FR-15 | C-G8 | TC-FR15-67 | BUG-36 #182 | [#314](https://github.com/tkob-team/eshop-sut/issues/314) |
| BUG-103 | C – FR-15 | C-G9 | TC-FR15-78 | BUG-37 #183 (+ annotation BUG-48 #194) | [#315](https://github.com/tkob-team/eshop-sut/issues/315) |

Tổng: 18 bug (A 3, B 6, C 9). Đã tạo 18 issue (2026-11-17, tài khoản ThachHaoo, label `bug`; ảnh nhúng bằng link raw @ `b264556`). Lệnh đã dùng: `gh issue create --repo tkob-team/eshop-sut --body-file HW04/bugs/BUG-xx.md --label bug --title "[HW04][FR-xx] …"` — chỉ chạy khi SV đã viết xong file.
