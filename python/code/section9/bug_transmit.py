"""
异常的传递性
"""


# 定义一个出现异常的函数

def func1():
    print("func1开始执行")
    num = 1 / 0
    print("func1执行完成")


# 定义一个无异常的方法，调用上面的方法
def func2():
    print("func2开始执行")
    func1()
    print("func2执行结束")


def mian():
    try:
        func2()
    except Exception as e:
        print(f"太low了，出现bug了，bug是：{e}")
    else:
        num1 = num + 1
    finally:
        print("我是大哥，都可以执行")


mian()
