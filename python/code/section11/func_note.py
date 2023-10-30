# _*_ coding:UTF-8 _*_
"""
演示函数（方法）进行类型注解
"""

# 对形参进行类型注解
def add(x:int,y:int):
    return x+y

print(add(3,4))
# 对返回值进行类型注解
def func(data:list)->list:
    return data

func([1,2])