"""
打印九九乘法表
"""
"""
print("Hello\tworld")
print("Hellola\tbest")

print("Hello",end=' ')
print("world")
"""

i = 1

while i <= 9:
    j = 1
    while j <= i:
        amass = i * j
        #通过 \t 制表符进行对齐， end='' 进行控制不换行
#        print(j, "*", i,"=", amass,'\t', end='')
        print(f"{j}*{i}={amass}\t",end='')
        j += 1
    print()
    i += 1
