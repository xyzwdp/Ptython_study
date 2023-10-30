# _*_ coding:UTF-8 _*_
"""
演示面向对象封装思想中私有成员的使用
"""

# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage=0

    def __keep_single__core(self):
        print("让CPU单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage>=1:
            print("5g通话已开启")
        else:
            self.__keep_single__core()
            print("电量不足，无法使用5g通话，并设置为单核运行进行省电")
phone=Phone()
# 私有成员方法与成员变量无法在类外调用
# phone.__keep_single__core()
print(phone.__current_voltage)

# 私有成员方法与成员变量可以在类内部调用
phone.call_by_5g()