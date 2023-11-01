"""
for 循环临时变量的作用域
"""

# 定义变量

i = 0

# i可以访问到，但是不建议使用

for i in range(2):
    print(i)

print(i)
