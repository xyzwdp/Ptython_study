# _*_ coding:UTF-8 _*_
"""
魔术方法演示学习
"""

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def __str__(self):
    #     return f"Student对象，name：{self.name}，age：{self.age}"

    def __lt__(self, other):
        print(self.age)
        print(other.age)
        return self.age<other.age

    def __le__(self, other):
        return self.age<=other.age

    def __eq__(self, other):
        return self.name==other.name



# __str__魔术方法
# stu=Student("张三",33)
# print(stu)
# print(str(stu))

# __lt__魔术方法，less, 小于，大于比较
# stu1=Student("张三",33)
# stu2=Student("李四",44)
# print(stu1<stu2)
# print(stu1>stu2)

# __le__魔术方法，equal，小于等于，大于等于比较
# stu1=Student("张三",33)
# stu2=Student("李四",44)
# # 真真得真
# print(stu1<=stu2)
# # 真假得假
# print(stu1>=stu2)

# __eq__魔术方法，符号比较
stu1=Student("张三",33)
stu2=Student("张三",44)
print(stu1==stu2)