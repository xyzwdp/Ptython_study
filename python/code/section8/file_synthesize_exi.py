"""
文件操作综合练习
"""

"""
·读取文件

·将文件写出到bill.txt.bak文件作为备份

·同时，将文件内标记为测试的数据行丢弃

实现思路：

·open和r模式打开一个文件对象，并读取文件

·open和w模式打开另一个文件对象，用于文件写出

·for循环内容，判断是否是测试不是测试就write写出，是测试就continue跳过

·将2个文件对象均close（）
"""

with open("E:\\python\\docunmentation\\money.txt", 'r', encoding='UTF-8') as fr:
    for countent in fr:
        # print(countent)
        my_cum = countent.strip().split("，")
        # print(type(my_cum))
        # print(my_cum)
        if my_cum.pop(4)=="测试":
            # print(countent)
            continue
        with open("E:\\python\\docunmentation\\money.bak.txt", 'a', encoding='UTF-8') as fw:
            fw.write(countent)

