# _*_ coding:UTF-8 _*_
# 设计一个类（类比生活中：设计一张等级表）
class Student():
    name = None
    gender = None
    nationlity = None
    native_place = None
    age = None


# 创建一个对象（类比生活中：打印一张登记表）
stu1 = Student()

# 对象属性进行赋值（类比生活中：填写表单）
stu1.name = "张三"
stu1.gender = "不男不女"
stu1.nationlity = "中国"
stu1.native_place = "月球"
stu1.age = 900

# 获取对象中记录的信息
print(stu1.name)
print(stu1.gender)
print(stu1.nationlity)
print(stu1.native_place)
print(stu1.age)
