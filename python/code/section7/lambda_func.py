"""
lanbda匿名函数
"""


# 定义一个函数，接收他的函数输入
def test_func(compute):
    result = compute(2, 3)
    print(f'compute参数的类型是：{type(compute)}')
    print(f"计算结果是：{result}")


# 通 入
test_func(lambda x, y: x * y)
