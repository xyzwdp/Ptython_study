"""
遍历列表元素遍历
"""


def list_while_func():
    """
    使用while循环遍历列表演示函数
    :return: None
    """
    mylist = ['测试工程师', '广州', 15000]

    index = 0
    while index < len(mylist):
        element = mylist[index]
        print(f"列表第{index}元素值为：{element}")
        index += 1


list_while_func()


def list_for_func():
    """
    使用for循环遍历列表演示函数
    :return: None
    """
    mylist = ['测试工程师', '广州', 15000]
    index = 1
    for ele in mylist:
        print(f"列表第{index}元素值为：{ele}")
        index += 1


list_for_func()
