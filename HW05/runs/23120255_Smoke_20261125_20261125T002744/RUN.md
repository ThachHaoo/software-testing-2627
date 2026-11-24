# RUN – 23120255_Smoke_20261125

| Mục | Giá trị |
|---|---|
| Lượt chính thức | KHÔNG (lượt thử / smoke – export-ignore khi nộp) |
| Ghi chú | T1-4 smoke lần 2 (sau S1) |
| Hostname | LAPTOP-NFIGFMR1 |
| CPU / luồng logic | 13th Gen Intel(R) Core(TM) i5-13500H / 16 |
| Bắt đầu JMeter (ISO) | 2026-11-25T00:27:47.9670427+07:00 |
| Kết thúc JMeter (ISO) | 2026-11-25T00:29:07.5966527+07:00 |
| Restart backend lúc | 2026-11-25T00:27:46.7458196+07:00 |
| PID backend (node) / JMeter (java) | 12496 / 9932 |
| Test plan | `D:\HK7\Testing\Exercise\HW\software-testing-2627\HW05\testplans\23120255_Smoke_20261125.jmx` |
| sha256 test plan | `0729627346f93953b1dd333b4b11c98d1cafab0d18e5d8b9debbd0223b7daf22` |
| Commit repo / SUT | `b8c96ad` / `de0f48f` |
| JMeter / Java | D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3 / openjdk version "25.0.3" 2026-04-21 LTS |
| Heap JMeter | `-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m` |
| RAM trống lúc bắt đầu / tổng | 2729 MB / 16017 MB |
| Exit code JMeter | 0 |
| jtl | `23120255_Smoke_20261125.jtl` – 549 dòng, 87814 byte |
| HTML report | `html/index.html` (số liệu: `html/statistics.json`) |
| Giám sát tài nguyên | `monitor.csv` (mỗi 1 s, theo PID; cpu_pct_machine = % của cả máy, 16 luồng logic) |

Lệnh JMeter:

```
java -Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m -jar D:\apache-jmeter-5.6.3\apache-jmeter-5.6.3\bin\ApacheJMeter.jar -n -t D:\HK7\Testing\Exercise\HW\software-testing-2627\HW05\testplans\23120255_Smoke_20261125.jmx -l D:\HK7\Testing\Exercise\HW\software-testing-2627\HW05\runs\23120255_Smoke_20261125_20261125T002744\23120255_Smoke_20261125.jtl -e -o D:\HK7\Testing\Exercise\HW\software-testing-2627\HW05\runs\23120255_Smoke_20261125_20261125T002744\html -j D:\HK7\Testing\Exercise\HW\software-testing-2627\HW05\runs\23120255_Smoke_20261125_20261125T002744\jmeter.log -Jjmeter.save.saveservice.output_format=csv
```

Các bước reset trước lượt: dừng tiến trình nghe cổng 3000 → `node server.js` (CSDL DROP + seed lại, mất user đăng ký thêm và trạng thái khoá) → chờ `GET /api/products` = 200.
