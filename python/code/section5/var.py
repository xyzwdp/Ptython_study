"""
变量
"""


def var_a():
    num = 100
    print(num)


var_a()
# 函数体外，局部变量无法使用
# print(num)

a = 20


def var_b(b):
    """

    Args:
        b: 形参，传入值为数值

    Returns:返回值为一个数值

    """
    b = 50
    z=a+b
    print(a)
    return z


def var_c():
    """
    global修改全局变量值
    :return:
    """
    global a
    a = 60
    print(a)


var_b()
var_c()
# 全局变量在函数内外都可以使用
print(a)
