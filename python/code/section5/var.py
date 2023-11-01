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


def var_b():
    a = 50
    print(a)


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
