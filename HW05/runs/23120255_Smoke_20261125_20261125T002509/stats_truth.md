# stats_truth – `23120255_Smoke_20261125.jtl`

549 dòng · percentile: commons-math legacy p(n+1)

| Label | count | errors | error % | mean | min | max | p50 | p90 | p95 | p99 | req/s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total | 549 | 80 | 14.57 | 8.56 | 2 | 128 | 8.00 | 11.00 | 14.00 | 27.50 | 8.739 |
| 00_setup_register_lockout | 20 | 0 | 0.00 | 16.25 | 8 | 128 | 10.00 | 13.90 | 122.30 | 128.00 | 45.249 |
| 00_setup_register_user | 400 | 0 | 0.00 | 9.37 | 5 | 128 | 9.00 | 12.00 | 14.00 | 28.97 | 93.284 |
| 01_POST_login | 13 | 0 | 0.00 | 4.77 | 3 | 11 | 4.00 | 9.00 | 11.00 | 11.00 | 0.235 |
| 02_GET_products | 12 | 0 | 0.00 | 3.75 | 3 | 5 | 4.00 | 5.00 | 5.00 | 5.00 | 0.250 |
| 03_POST_checkout | 12 | 0 | 0.00 | 13.75 | 8 | 25 | 13.00 | 23.50 | 25.00 | 25.00 | 0.249 |
| 04_GET_my_orders | 12 | 0 | 0.00 | 4.00 | 2 | 6 | 4.00 | 5.70 | 6.00 | 6.00 | 0.246 |
| L1_POST_login_sai_1 | 20 | 20 | 100.00 | 4.40 | 3 | 10 | 4.00 | 5.90 | 9.80 | 10.00 | 0.514 |
| L2_POST_login_sai_2 | 20 | 20 | 100.00 | 3.85 | 2 | 7 | 4.00 | 5.00 | 6.90 | 7.00 | 0.514 |
| L3_POST_login_sai_3 | 20 | 20 | 100.00 | 3.70 | 2 | 7 | 3.00 | 5.90 | 6.95 | 7.00 | 0.514 |
| L4_POST_login_dung_khi_khoa | 20 | 20 | 100.00 | 3.45 | 2 | 6 | 3.00 | 4.90 | 5.95 | 6.00 | 0.514 |

## Timeline theo phút

| Phút | count | lỗi | mean | p95 | max threads |
|---|---|---|---|---|---|
| 0 | 545 | 80 | 8.6 | 14.0 | 3 |
| 1 | 4 | 0 | 5.0 | 10.0 | 2 |

## Lỗi hay gặp

| Label | code | thông báo | số lần |
|---|---|---|---|
| L1_POST_login_sai_1 | 401 | Unauthorized | 20 |
| L2_POST_login_sai_2 | 401 | Unauthorized | 20 |
| L3_POST_login_sai_3 | 403 | Forbidden | 20 |
| L4_POST_login_dung_khi_khoa | 403 | Forbidden | 20 |

## Đối chiếu `HW05/runs/23120255_Smoke_20261125_20261125T002509/html/statistics.json`

Lệch tương đối lớn nhất: **0.00%**

| Label | chỉ số | jtl_stats | statistics.json | chênh | % |
|---|---|---|---|---|---|
| Total | count | 549.000 | 549.000 | +0.000 | 0.00% |
| Total | errors | 80.000 | 80.000 | +0.000 | 0.00% |
| Total | error % | 14.572 | 14.572 | -0.000 | 0.00% |
| Total | mean | 8.565 | 8.565 | +0.000 | 0.00% |
| Total | min | 2.000 | 2.000 | +0.000 | 0.00% |
| Total | max | 128.000 | 128.000 | +0.000 | 0.00% |
| Total | p50 | 8.000 | 8.000 | +0.000 | 0.00% |
| Total | p90 | 11.000 | 11.000 | +0.000 | 0.00% |
| Total | p95 | 14.000 | 14.000 | +0.000 | 0.00% |
| Total | p99 | 27.500 | 27.500 | +0.000 | 0.00% |
| Total | req/s | 8.739 | 8.739 | -0.000 | 0.00% |
| 00_setup_register_lockout | count | 20.000 | 20.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | errors | 0.000 | 0.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | error % | 0.000 | 0.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | mean | 16.250 | 16.250 | +0.000 | 0.00% |
| 00_setup_register_lockout | min | 8.000 | 8.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | max | 128.000 | 128.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | p50 | 10.000 | 10.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | p90 | 13.900 | 13.900 | -0.000 | 0.00% |
| 00_setup_register_lockout | p95 | 122.300 | 122.300 | +0.000 | 0.00% |
| 00_setup_register_lockout | p99 | 128.000 | 128.000 | +0.000 | 0.00% |
| 00_setup_register_lockout | req/s | 45.249 | 45.249 | +0.000 | 0.00% |
| 00_setup_register_user | count | 400.000 | 400.000 | +0.000 | 0.00% |
| 00_setup_register_user | errors | 0.000 | 0.000 | +0.000 | 0.00% |
| 00_setup_register_user | error % | 0.000 | 0.000 | +0.000 | 0.00% |
| 00_setup_register_user | mean | 9.373 | 9.372 | +0.000 | 0.00% |
| 00_setup_register_user | min | 5.000 | 5.000 | +0.000 | 0.00% |
| 00_setup_register_user | max | 128.000 | 128.000 | +0.000 | 0.00% |
| 00_setup_register_user | p50 | 9.000 | 9.000 | +0.000 | 0.00% |
| 00_setup_register_user | p90 | 12.000 | 12.000 | +0.000 | 0.00% |
| 00_setup_register_user | p95 | 14.000 | 14.000 | +0.000 | 0.00% |
| 00_setup_register_user | p99 | 28.970 | 28.970 | +0.000 | 0.00% |
| 00_setup_register_user | req/s | 93.284 | 93.284 | +0.000 | 0.00% |
| 01_POST_login | count | 13.000 | 13.000 | +0.000 | 0.00% |
| 01_POST_login | errors | 0.000 | 0.000 | +0.000 | 0.00% |
| 01_POST_login | error % | 0.000 | 0.000 | +0.000 | 0.00% |
| 01_POST_login | mean | 4.769 | 4.769 | +0.000 | 0.00% |
| 01_POST_login | min | 3.000 | 3.000 | +0.000 | 0.00% |
| 01_POST_login | max | 11.000 | 11.000 | +0.000 | 0.00% |
| 01_POST_login | p50 | 4.000 | 4.000 | +0.000 | 0.00% |
| 01_POST_login | p90 | 9.000 | 9.000 | +0.000 | 0.00% |
| 01_POST_login | p95 | 11.000 | 11.000 | +0.000 | 0.00% |
| 01_POST_login | p99 | 11.000 | 11.000 | +0.000 | 0.00% |
| 01_POST_login | req/s | 0.235 | 0.235 | +0.000 | 0.00% |
| 02_GET_products | count | 12.000 | 12.000 | +0.000 | 0.00% |
| 02_GET_products | errors | 0.000 | 0.000 | +0.000 | 0.00% |
| 02_GET_products | error % | 0.000 | 0.000 | +0.000 | 0.00% |
| 02_GET_products | mean | 3.750 | 3.750 | +0.000 | 0.00% |
| 02_GET_products | min | 3.000 | 3.000 | +0.000 | 0.00% |
| 02_GET_products | max | 5.000 | 5.000 | +0.000 | 0.00% |
| 02_GET_products | p50 | 4.000 | 4.000 | +0.000 | 0.00% |
| 02_GET_products | p90 | 5.000 | 5.000 | +0.000 | 0.00% |
| 02_GET_products | p95 | 5.000 | 5.000 | +0.000 | 0.00% |
| 02_GET_products | p99 | 5.000 | 5.000 | +0.000 | 0.00% |
| 02_GET_products | req/s | 0.250 | 0.250 | -0.000 | 0.00% |
| 03_POST_checkout | count | 12.000 | 12.000 | +0.000 | 0.00% |
| 03_POST_checkout | errors | 0.000 | 0.000 | +0.000 | 0.00% |
| 03_POST_checkout | error % | 0.000 | 0.000 | +0.000 | 0.00% |
| 03_POST_checkout | mean | 13.750 | 13.750 | -0.000 | 0.00% |
| 03_POST_checkout | min | 8.000 | 8.000 | +0.000 | 0.00% |
| 03_POST_checkout | max | 25.000 | 25.000 | +0.000 | 0.00% |
| 03_POST_checkout | p50 | 13.000 | 13.000 | +0.000 | 0.00% |
| 03_POST_checkout | p90 | 23.500 | 23.500 | -0.000 | 0.00% |
| 03_POST_checkout | p95 | 25.000 | 25.000 | +0.000 | 0.00% |
| 03_POST_checkout | p99 | 25.000 | 25.000 | +0.000 | 0.00% |
| 03_POST_checkout | req/s | 0.249 | 0.249 | +0.000 | 0.00% |
| 04_GET_my_orders | count | 12.000 | 12.000 | +0.000 | 0.00% |
| 04_GET_my_orders | errors | 0.000 | 0.000 | +0.000 | 0.00% |
| 04_GET_my_orders | error % | 0.000 | 0.000 | +0.000 | 0.00% |
| 04_GET_my_orders | mean | 4.000 | 4.000 | +0.000 | 0.00% |
| 04_GET_my_orders | min | 2.000 | 2.000 | +0.000 | 0.00% |
| 04_GET_my_orders | max | 6.000 | 6.000 | +0.000 | 0.00% |
| 04_GET_my_orders | p50 | 4.000 | 4.000 | +0.000 | 0.00% |
| 04_GET_my_orders | p90 | 5.700 | 5.700 | -0.000 | 0.00% |
| 04_GET_my_orders | p95 | 6.000 | 6.000 | +0.000 | 0.00% |
| 04_GET_my_orders | p99 | 6.000 | 6.000 | +0.000 | 0.00% |
| 04_GET_my_orders | req/s | 0.246 | 0.246 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | count | 20.000 | 20.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | errors | 20.000 | 20.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | error % | 100.000 | 100.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | mean | 4.400 | 4.400 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | min | 3.000 | 3.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | max | 10.000 | 10.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | p50 | 4.000 | 4.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | p90 | 5.900 | 5.900 | -0.000 | 0.00% |
| L1_POST_login_sai_1 | p95 | 9.800 | 9.800 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | p99 | 10.000 | 10.000 | +0.000 | 0.00% |
| L1_POST_login_sai_1 | req/s | 0.514 | 0.514 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | count | 20.000 | 20.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | errors | 20.000 | 20.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | error % | 100.000 | 100.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | mean | 3.850 | 3.850 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | min | 2.000 | 2.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | max | 7.000 | 7.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | p50 | 4.000 | 4.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | p90 | 5.000 | 5.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | p95 | 6.900 | 6.900 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | p99 | 7.000 | 7.000 | +0.000 | 0.00% |
| L2_POST_login_sai_2 | req/s | 0.514 | 0.514 | -0.000 | 0.00% |
| L3_POST_login_sai_3 | count | 20.000 | 20.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | errors | 20.000 | 20.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | error % | 100.000 | 100.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | mean | 3.700 | 3.700 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | min | 2.000 | 2.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | max | 7.000 | 7.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | p50 | 3.000 | 3.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | p90 | 5.900 | 5.900 | -0.000 | 0.00% |
| L3_POST_login_sai_3 | p95 | 6.950 | 6.950 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | p99 | 7.000 | 7.000 | +0.000 | 0.00% |
| L3_POST_login_sai_3 | req/s | 0.514 | 0.514 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | count | 20.000 | 20.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | errors | 20.000 | 20.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | error % | 100.000 | 100.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | mean | 3.450 | 3.450 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | min | 2.000 | 2.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | max | 6.000 | 6.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | p50 | 3.000 | 3.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | p90 | 4.900 | 4.900 | -0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | p95 | 5.950 | 5.950 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | p99 | 6.000 | 6.000 | +0.000 | 0.00% |
| L4_POST_login_dung_khi_khoa | req/s | 0.514 | 0.514 | +0.000 | 0.00% |
