import csv


def read_orders(file_name):
    orders = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["id"] = int(row["id"])
                    row["amount"] = float(row["amount"])
                    orders.append(row)
                except (ValueError, TypeError):
                    print("跳过错误数据：", row)

    except FileNotFoundError:
        print(f"找不到文件：{file_name}")

    return orders


def calculate_paid_amount(order_list):
    total_amount = 0

    for order in order_list:
        if order["status"] == "已支付":
            total_amount += order["amount"]

    return total_amount


orders = read_orders("orders.csv")
paid_amount = calculate_paid_amount(orders)

print("成功读取订单数：", len(orders))
print("已支付销售额：", paid_amount)