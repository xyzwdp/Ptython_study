# _*_ coding:UTF-8 _*_
"""
演示构造方法
"""

# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__

class Student:
    # 成员变量定义可以不写
    # name=None
    # age=None
    # tel=None
    def __init__(self,name,age,tel):
        # Young赋值与定义功能
        self.name=name
        self.age=age
        self.tel=tel
        print("Student类创建了一个类对象")

    def say_hi(self):
        print(f"我的名字叫{self.name}")

stu=Student("张三",88,110119120)
print(stu.name)
print(stu.age)
print(stu.tel)

stu.say_hi()