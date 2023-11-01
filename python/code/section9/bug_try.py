"""
捕获异常
"""

"""
了解异常
"""

# 基本语法捕获异常
try:
    f = open("E:\\python\\docunmentation\\bug.txt", 'r', encoding="UTF-8")
except:
    print(f"出现异常，文件不存在，我们将open的 r 读模式，改为 w 写模式打开文件")
    f = open("E:\\python\\docunmentation\\bug.txt", 'w', encoding="UTF-8")

# 捕获指定异常
try:
    print(name)
    # 1/0
except NameError as e:
    print("出现变量未定义的异常")
    print(e)
print('------------------------')

# 捕获多个异常
try:
    # print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义 或者 除以0 的异常")
    print(e)
print("--------------------")

# 未正确设置捕获异常类型，将无法捕获异常

# 捕获所有异常
try:
    # 1/0
    print(name)
except Exception as e:
    print("出现异常了吗")
    print(e)
print('========================')

# 未捕获到异常可执行语句----else
try:
    print("Hello World")
except Exception as e:
    print('出现异常')
else:
    print('躲过except')
print("===========================")

# 不管是否捕获到异常都执行----finally
try:
    f = open("E:\\python\\docunmentation\\except.txt", 'r', encoding="UTF-8")
except Exception as e:
    print('出现异常了')
    f = open("E:\\python\\docunmentation\\except.txt", 'w', encoding="UTF-8")
else:
    print('好巧，没有bug')
finally:
    f.close()

