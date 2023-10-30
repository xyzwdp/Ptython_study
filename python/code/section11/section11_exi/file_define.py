# _*_ coding:UTF-8 _*_

"""
和文件相关类定义
"""
from __future__ import annotations

import json

from data_define import Record



# 定义一个抽象类用来作顶层设计，确定有那些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        # 读取文件数据，督导的每一条数据转换为Record对象，将他们封装在list内返回即可
        pass

    # def __str__(self):
    #     return self.read_data()


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件的路径
        # self.record_list=record_list

    # def __str__(self):
    #     return self.record_list
    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        with open(self.path, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                line = line.strip()  # 消除每一行数据中的\n
                # print(line)
                data_list = line.split(",")
                # print(data_list)
                # 转为元组
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                # print(record)
                # 每个元组添加在列表中
                record_list.append(record)
                print(f"{record_list}")
        return record_list


class JsonFileReader:
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        with open(self.path, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                data_dict = json.loads(line)
                # print(data_dict)
                record = Record(data_dict["date"], data_dict["order_id"], int(data_dict['money']),
                                data_dict["province"])
                # print(record)
                record_list.append(record)
        # print(record_list)
        return record_list


if __name__ == '__main__':
    list_1=TextFileReader("E:\\test\\python_data\\资料\\第13章资料\\2011年1月销售数据.txt").read_data()
    list_2=JsonFileReader("E:\\test\\python_data\\资料\\第13章资料\\2011年2月销售数据JSON.txt").read_data()
    # for l in list_1:
    #     print(l)
    #
    # for l in list_2:
    #     print(l)
    # # print(list_1)