"""
文件读取
"""
import time

# import time

# 打开文件---open()
f = open("E:\\python\\docunmentation\\python.txt.txt", "r", encoding='UTF-8')
print(type(f))

# 读取文件---read()
# 连续读取内容，第二次读取会在第一次读取之后继续读取
# print(f"读取10字节的结果：{f.read(10)}")
print(f"读取全部内容：{f.read()}")
print("-----------------------------")

# # 读取文件---readlines()
# # 读取文件全部行，封装在列表中
# # lins = f.readlines()
# # print(f"lins对象的类型：{type(lins)}")
# # print(f"lins对象的全部内容：{lins}")
# # print("---------------------------")
#
# # 读取文件----readline()
# # 每次调用读取一行数据,类型为字符串类型
# # line1 = f.readline()
# # line2 = f.readline()
# # line3 = f.readline()
# # print(f"line1对象的类型：{type(line1)}")
# # print(f"line1对象的全部内容：{line1}")
# # print(f"line2对象的全部内容：{line2}")
# # print(f"line3对象的全部内容：{line3}")
# # print("---------------------------")
#
# # for循环读取文件行
# # 读取结果类型是字符串
# i = 1
# for line in f:
#     print(f"第{i}行数据是：{line}")
#     print(f"读取结果类型是：{type(line)}")
#     i += 1
# # 文件的关闭
# # 解决文件占用
#
# f.close()
# time.sleep(5000)
# print('------------------------')
# with open 语法操作文件
# 返回类型是字符串
# (as f) 文件执行完成会自动关闭文件
# with open("E:\\python\\docunmentation\\python.txt.txt", "r", encoding='UTF-8') as f:
#     i = 1
#     for line in f:
#         print(f"第{i}行数据是：{line}")
#         print(f"读取结果类型是：{type(line)}")
#         i += 1
# time.sleep(5000)

