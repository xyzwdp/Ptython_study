"""
演示input()语句
获取键盘输入信息
"""

print("请告诉我你是谁？")

name = input()

print("原来你是：%s" % name)

print("请告诉我你的银行卡密码？")

pasw = input("是你的银行卡密码哦：")

finel = int(pasw)

print(pasw)

print("你的银行卡类型是：", type(pasw))

print("你的银行卡类型是：", type(finel))
