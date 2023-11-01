"""
传参的演示
"""


def add(x,y):
    """
    两数相加
    :param x:形参的一个数字
    :param y:形参的另外一个数字
    :return:为两个数的和
    """
    result=x+y
    print(f"{x}+{y}的和是：{result}")

add(3,4)


def tem(t):
    if t>37.5:
        print(f"你的体温是{t},快去西天请如来佛主！！")
    else:
        print(f"你的体温是{t},金主爸爸来了，欢迎光临！！！")


tem(40)

tem(37)