"""
默认返回值None

"""


def say_hi():
    print("beautiful")
    return None


result = say_hi()
print(f"无返回值函数，返回内容是：{result}")
print(f"无返回值函数，返回内容类型是：{type(result)}")

"""
None用于if判断
    在if判断中，None等同于False
    一般用户函数主动返回None，配合if判断相关处理
"""


def check_age(age):
    if age > 18:
        return "success"
    # else:
    #     return None


result = check_age(19)

if not result:
    print("未成年，不可进入")

if not result  is None:
    print("未成年，不可进入!!")

if result is not None:
    print("休息")

if result is not None:
    print("什么结果")

"""
None用于声明无初始内容的变量
"""

name = None
