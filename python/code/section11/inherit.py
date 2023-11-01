# _*_ coding:UTF-8 _*_
"""
面向对象，继承的基础语法
"""


# 演示单继承
# class Phone:
#     IMEI=None
#     producer="xiaomi"
#
#     def call_by_4g(self):
#         print("4g通话")
#
# class Phone2023(Phone):
#     face_id="1001"
#     def call_by_5g(self):
#         print("2023年新功能：5g通话")
#
# phone2023=Phone2023()
# print(phone2023.producer)
# phone2023.call_by_4g()
# phone2023.call_by_5g()

# 演示多继承
class Phone1:
    IMEI = None
    producer = "xiaomi"

    def call_by_3g(self):
        print("3g通话")

class Phone(Phone1):
    IMEI = None
    producer = "xiaomi"

    def call_by_4g(self):
        print("4g通话")


class NFCReader:
    nfc_type = "第五代"
    producer = "vivo"

    def red_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    # 补全语法
    pass

myphone=MyPhone()
myphone.call_by_4g()
myphone.red_card()
myphone.write_card()
myphone.control()
myphone.call_by_3g()

# 演示多继承下，父类成员名一致的场景
# 左边先继承，先使用左边数据，先继承的优先级高于后继承
print(myphone.producer)