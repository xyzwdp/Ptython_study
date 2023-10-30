# _*_ coding:UTF-8 _*_
"""
导入包操作
"""
#创建一个包
# 导入自定义包中模块，并使用
# from my_Packge.my_module5 import test1
# import my_Packge.my_module6
# # from my_Packge import my_module6
#
# test1()
# my_Packge.my_module6.test2()

# 通过__all__变量，控制import *
from my_Packge import *
my_module5.test1()
my_module6.test2()

