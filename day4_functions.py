orders = [
    {"id": 1, "amount": 99.9, "status": "已支付"},
    {"id": 2, "amount": 158.0, "status": "已退款"},
    {"id": 3, "amount": 36.5, "status": "已支付"},
    {"id": 4, "amount": 299.0, "status": "待支付"},
    {"id": 5, "amount": 88.0, "status": "已支付"}
]
def calculate_paid_summary(order_list):
    paid_count = 0
    paid_amount = 0
    refund_count = 0

    for order in order_list:
        if order["status"] == "已支付":
            paid_count = paid_count + 1
            paid_amount = paid_amount + order["amount"]
        elif order["status"] == "已退款":
            refund_count = refund_count + 1

    if paid_count == 0:
        average_amount = 0
    else:
        average_amount = paid_amount / paid_count

    return paid_count, paid_amount, average_amount, refund_count


count, total, average, refund = calculate_paid_summary(orders)
print("已支付订单数：", count)
print("已支付销售额：", total)
print("已支付平均订单金额：", average)
print("退款订单数：", refund)

order_list = [
    {"id": 1, "amount": 99.9, "status": "已支付"},
    {"id": 2, "amount": 158.0, "status": "已退款"},
    {"id": 3, "amount": 36.5, "status": "已支付"},
    {"id": 4, "amount": 299.0, "status": "待支付"},
    {"id": 5, "amount": 88.0, "status": "已支付"}
]

def get_large_paid_orders(order_list, threshold):
    large_orders = []
    for order in order_list:
        if order["status"] == "已支付" and order["amount"] > threshold:
            large_orders.append(order)
    return large_orders
print("大额已支付订单：", get_large_paid_orders(orders, 100))