# _*_ coding:UTF-8 _*_
"""
自定义模块
"""

#导入自定义模块使用
# import my_module1
# my_module1.test(1,2)

# from my_module1 import test
# test(1,3)

# 导入不同木块的同名功能
# from my_module1 import *
# from my_module3 import *
# test(3,4)

# __mian__变量
# from my_module1 import test
# test(3,4)

# __all__变量
from my_module4 import *
# from my_module4 import testA,testB
print(testA(1,4))
print(testB(5,6))

