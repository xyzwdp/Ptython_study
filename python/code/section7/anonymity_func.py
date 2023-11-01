"""
匿名函数
"""

# 定义一个函数，接收你一个函数作为传入参数
from anonymity_func_tow import add

# def test_func(compute):
#     result=compute(2,3)
#     print(f'compute参数的类型是：{type(compute)}')
#     print(f"计算结果是：{result}")
#
# # def compute(x, y):
# #     return x + y
#
# test_func(compute)
def test_func(compute):
    result=add(2,3)
    print(f'compute参数的类型是：{type(compute)}')
    print(f"计算结果是：{result}")

test_func(add)

