"""Dựng đơn cho lượt chạy tay (cùng dữ liệu như ensureOrders() của Playwright), chỉ dùng thư viện chuẩn.

    python HW03/tests/seed_orders.py                      # dựng đơn
    python HW03/tests/seed_orders.py --restore-password   # đặt lại mật khẩu test@eshop.com = Test1234!

Tạo 7 đơn của test@eshop.com: 5 đơn ở đủ 5 trạng thái (Chờ xác nhận, Đã xác nhận, Đang giao, Đã giao, Đã hủy – CL-58/CL-59)
+ 2 đơn Chờ xác nhận để thử huỷ (CL-60, CL-61). Chạy SAU khi đã kiểm empty state (CL-62). In bảng mã đơn ↔ trạng thái.
"""
import json, sys, urllib.request

API = "http://localhost:3000"
for s in (sys.stdout,):
    try:
        s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def call(method, path, body=None, token=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode() or "null")


def login(email, pw):
    return call("POST", "/api/login", {"email": email, "password": pw})["token"]


if "--restore-password" in sys.argv:   # sau CL-29 / CL-48 / CL-27: đặt lại mật khẩu seed qua API
    t = call("POST", "/api/forgot-password", {"email": "test@eshop.com"})["resetToken"]
    call("POST", "/api/reset-password", {"email": "test@eshop.com", "resetToken": t, "newPassword": "Test1234!"})
    login("test@eshop.com", "Test1234!")
    print("Đã đặt lại mật khẩu test@eshop.com = Test1234!")
    sys.exit(0)

u, a = login("test@eshop.com", "Test1234!"), login("admin@eshop.com", "Admin123!")
if call("GET", "/api/orders/my-orders", token=u):
    sys.exit("test@eshop.com đã có đơn — restart backend (CSDL seed) rồi chạy lại.")
ids = {}
for k in ["pending", "confirmed", "shipping", "delivered", "canceled", "cancelA", "cancelB"]:
    ids[k] = call("POST", "/api/checkout", {"items": [{"id": 4, "name": "Tai nghe AirPods Pro 2", "price": 6000000, "quantity": 1}],
                                            "total_amount": 6000000}, u)["orderId"]
for k, path in [("confirmed", ["confirmed"]), ("shipping", ["confirmed", "shipping"]),
                ("delivered", ["confirmed", "shipping", "delivered"]), ("canceled", ["canceled"])]:
    for s in path:
        call("PUT", f"/api/admin/orders/{ids[k]}/status", {"status": s}, a)
label = {"pending": "Chờ xác nhận", "confirmed": "Đã xác nhận", "shipping": "Đang giao", "delivered": "Đã giao",
         "canceled": "Đã hủy", "cancelA": "Chờ xác nhận – dùng cho CL-60", "cancelB": "Chờ xác nhận – dùng cho CL-61"}
for k, v in ids.items():
    print(f"#{v}\t{label[k]}")
