"""
变量练习
"""


def while_tar():
    """
    使用while循环遍历列表取出偶数
    :return: None
    """
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    index = 0
    while index < len(mylist):
        ele = mylist[index]
        if ele % 2 == 0:
            new_list.append(ele)

        index += 1
    print(f"偶数集列表为{new_list}")

while_tar()


def for_sar():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = list()
    for ele in mylist:
        if ele%2==0:
            new_list.append(ele)

    print(f"偶数集列表为{new_list}")

for_sar()