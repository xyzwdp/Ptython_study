# _*_ coding:UTF-8 _*_
"""
演示变量的类型注解
"""
from __future__ import annotations

import json
import random

# 基础数据类型注解
var_1: int = 10
var_2: str = "张三"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型详细注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"李四": 666}

# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, str, bool] = (1, "张三", True)
my_dict1: dict[str, int] = {"李四": 666}

# 在注释中进行类型注解
var_4 = random.randint(1, 10)  # type:int
var_5 = json.loads('{"name":"张三"}')  # type:dict[str,str]


def func():
    return 10


var_6 = func()  # type:int

# 类型注解的限制
var_7: int = "李四"
var_8: str = 123
