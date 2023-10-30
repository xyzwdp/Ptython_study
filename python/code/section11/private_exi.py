# _*_ coding:UTF-8 _*_
"""
封装中私有成员方法与变量练习
"""
class Phone:
    __is_5g_enable = True
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4g网络")

    def call_by_5g(self):
        # if self.__is_5g_enable:
        #     self.__check_5g()
        #     print("正在通话中")
        # else:
        self.__check_5g()
        print("正在通话中")

phone=Phone()
phone.call_by_5g()