# _*_ coding:UTF-8 _*_
"""
复写练习
"""
class Phone:
    IMEI = None
    producer="xiaomi"

    def call_by_5g(self):
        print("5g通话吗")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "oppo"
    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # print("使用5g网络进行通话")
        # 方式1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)

        #方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

myphone=MyPhone()
# print(myphone.producer)
# myphone.call_by_5g()
# 在子类中，调用父类成员

# print(Phone.producer)
# Phone.call_by_5g("")

# 使用super()调用父类成员
# super不可以在类外调用
print(super().producer)
super().call_by_5g