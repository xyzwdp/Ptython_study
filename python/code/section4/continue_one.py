"""
continue关键字
中断本次循环

break关键字
结束循环
"""

# for i in range(5):
#     print("hello world")
#     for j in range(5):
#         print("lalallala")
#         continue
#         print("真的")
#     print("揍你")


for i in range(3):
    print("可执行")
    j=0
    while j<=100:
        print("可执行语句2")
        break
        print("不执行")

print("可执行语句1")