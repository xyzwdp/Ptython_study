# _*_ coding:UTF-8 _*_
"""
面向对象类中的成员方法定义与使用
"""
# 定义一个成员方法的类
class Student:
    name=None
    def say_hi(self):
        print(f"大家好，我是{self.name}！！！")

    def say_hi1(self,mesg):
        print(f"大家好，我是{self.name}，我是干{mesg}的！！！")


stu1=Student()
stu1.name="张三"
stu1.say_hi()

stu2=Student()
stu2.name="李四"
stu2.say_hi()

stu1.say_hi1("IT")

