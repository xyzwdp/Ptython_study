"""
Python模块导入
"""

# 使用import导入time模块使用sleep功能（函数）
import time

# 使用from导入time的sleep功能（函数）
print("等待前")
time.sleep(1)
print("等待后")

# 使用from导入time的sleep功能（函数）
# from time import sleep
# print("等待前")
# sleep(1)
# print("等待后")

# 使用 * 导入time的模块全部功能
# from time import *
# print("等待前")
# sleep(1)
# print("等待后")



# 使用as给特定功能加上别名

# from time import sleep as s
# print("等待前")
# s(1)
# print("等待后")
