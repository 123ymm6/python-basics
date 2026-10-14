orders = [
    {"id": 1, "amount": 99.9, "status": "已支付"},
    {"id": 2, "amount": 158.0, "status": "已退款"},
    {"id": 3, "amount": 36.5, "status": "已支付"},
    {"id": 4, "amount": 299.0, "status": "待支付"},
    {"id": 5, "amount": 88.0, "status": "已支付"}
]
paid_count = 0
refund_count = 0
paid_amount = 0
dd_count = 0
for order in orders:
    if order["status"] == "已支付":
        paid_count += 1
        paid_amount = paid_amount + order["amount"]
    elif order["status"] == "已退款":
        refund_count = refund_count + 1
    else :
        dd_count = dd_count +1
print()
print("订单总数：", len(orders))
print("已支付订单数：", paid_count)
print("已支付销售额：", paid_amount)
print("退款订单数：", refund_count)
print("待支付订单数：", dd_count)