# _*_ coding:UTF-8 _*_
"""
类和对象的关系，即面向对象的编程套路（思想）
"""

# 设计一个类
class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建2各闹钟对象并让其工作
clock1=Clock()
clock1.id="323232"
clock1.price=9.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()

clock2=Clock()
clock2.id="333232"
clock2.price=99.99
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()