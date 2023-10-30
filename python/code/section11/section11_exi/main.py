# _*_ coding:UTF-8 _*_
"""
面向对象，数据分析案例他，柱业务逻辑代码
"""
from __future__ import annotations
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record

"""
1、设计一个类，可以完成数据的封装

2、设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能

3、读取文件，生产数据对象

4、进行数据需求的逻辑计算（计算每一天的销售额）

5、通过PyEcharts进行图形绘制
"""

# class X:
#     def __init__(self,all_data=list()):
#         self.all_data=all_data
#
#     def __str__(self):
#         return self.all_data

text_file_reder = TextFileReader("E:\\test\\python_data\\资料\\第13章资料\\2011年1月销售数据.txt")
json_file_reder = JsonFileReader("E:\\test\\python_data\\资料\\第13章资料\\2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reder.read_data()
feb_data: list[Record] = json_file_reder.read_data()
# print(jan_data)

    # 将2各月份的数据合并为1各list来存储
all_data: list[Record] = jan_data + feb_data

# print(','.join(all_data))

# 开始进行数据计算
# {”2021-01-01“：1234}
data_dict1={}
for record1 in all_data:
    # print(record.data)
    # print(data_dict1.keys())
    if record1.data in data_dict1.keys():
        # 当前日期已经有记录了，所以记录作累加
        data_dict1[record1.data]+=record1.money
    else:
        data_dict1[record1.data]=record1.money

# print(data_dict1)


# if __name__ == '__main__':
#     x=X()
#     X()
