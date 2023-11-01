"""
·主菜单效果
--------------------主菜单--------------------
周杰轮，您好，欢迎来到黑马银行ATM。请选择操作：
查询余额［输入1］
存款 ［输入2］
取款 ［输入3］
退出 ［输入4］
请输入您的选择：

查询余额效果
--------------------查询余额--------------------
周杰轮，您好，您的余额剩余：5000000元存

存，取款效果
--------------------存款--------------------
周杰轮，您好，您存款50000元成功
周杰轮，您好，您的余额剩余：5050000元

--------------------取款--------------------
周杰轮，您好，您取款50000元成功
周杰轮，您好，您的余额剩余：4950000元
"""

# 定义用户余额与姓名
money = 5000000
#name = None

# 输入姓名

name=input("请输入你的姓名：")

#定义主菜单函数
def m_menu():
    print("--------------------主菜单--------------------")
    key_input = input("""
                查询余额\t\t［输入1］
                存款 \t\t［输入2］
                取款 \t\t［输入3］
                退出 \t\t［输入4］
                请输入您的选择：""")
    return key_input

#定义查询余额函数
def que(a):
    if a:
        print("--------------------查询余额--------------------")
    print(f"周杰轮，您好，您的余额剩余：{money}")

#定义存款函数
def sav(num):
    global money
    money +=num
    print("--------------------存款--------------------")
    print(f"{name}您好，您的余额剩余：{money}")

    que(False)
#定义取款函数
def get_money(num):
    global money
    money-=num
    print("--------------------取款--------------------")
    print(f"{name}您好，您取款{num}元成功")

    que(False)

#操作无限循环操作函数
def go():
    while True:
        keyboard_input=m_menu()
        if keyboard_input=="1":
            que(True)
            continue
        elif keyboard_input=="2":
            num =int(input("你需要存钱多少？请放钱"))
            sav(num)
            continue
        elif keyboard_input=="3":
            num = int(input("你需要取钱多少？请取走"))
            get_money(num)
            continue
        else:
            print("欢迎下次光临")
            break


go()