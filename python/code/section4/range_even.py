"""
求出100的偶数个数
"""

count = 0

for i in range(100):
    # print(i)
    if i % 2 == 0:
        count += 1

print(f"0-100含有{count}个偶数")
