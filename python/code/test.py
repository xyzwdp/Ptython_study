"""
演示：快速体验函数的开发与使用
需求：统计季父传的长度，不使用内置函数len()
"""

str1="hello world"
str2="hello xiaobudian"
str3="hello feizhu"

count=0
for i in str1:
    count+=1
print(f"字符串[{str1}]的长度是：{count}")

count=0
for j in str2:
    count+=1
print(f"字符串[{str2}]的长度是：{count}")

count=0
for k in str3:
    count+=1
print(f"字符串[{str3}]的长度是：{count}")
print("--------------------------------")

def my_len(data):
    count=0
    for i in data:
        count+=1

    print(f"字符串[{data}]的长度是：{count}")

my_len(str1)

my_len(str2)

my_len(str3)