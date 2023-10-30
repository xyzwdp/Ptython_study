# _*_ coding:UTF-8 _*_
"""
类练习
"""

class Student:
    def __init__(self):
        # range为左闭有开区间
        for i in range(1,11):
            print(f"请输入{i}位学生信息，总共需要录入10位学生信息")
            name=input("请输入学生姓名：")
            age=input("请输入学生年龄：")
            site=input("请输入学生地址：")
            print(f"学生{i}信息录入完成，信息为：【学生姓名：{name}，年龄：{age}，地址：{site}】")

stu=Student()