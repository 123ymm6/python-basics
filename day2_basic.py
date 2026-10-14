# 变量
name = "小明"
age = 22
city = "西安"
# 字符串
print(f"{name}今年{age}岁，来自{city}。")
# 列表：保存多个订单金额
amounts = [99.9, 158.0, 36.5, 299.0, 88.0]

print("订单数量：", len(amounts))
print("第一笔订单：", amounts[0])
print("订单总金额：", sum(amounts))

# 字典：保存一个用户的信息
user = {
    "姓名": "小明",
    "年龄": 22,
    "城市": "西安",
    "会员": True
}

print("用户姓名：", user["姓名"])
print("是否为会员：", user["会员"])