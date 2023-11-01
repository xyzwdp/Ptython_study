# _*_ coding:UTF-8 _*_
"""
演示Union联合类型注解
"""

# 使用Union类型，导包
from __future__ import annotations
from typing import Union

my_list: list[Union[int,str]]=[1,2,"张三"]
def func(data:Union[int,str])->Union[int,str]:
    pass

func(5)