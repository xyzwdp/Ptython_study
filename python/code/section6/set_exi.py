"""
集合练习
"""

# 定义一个空集合
# 最终的到元素去重的集合对象，并打印输出

set1=set()
print(f"空集合set1为：{set1}，集合类型是：{type(set1)}")
print('--------------------------')

# 通过 for 循环列表
my_list=['张三','李四','张三','李四','Python','Python']
for element in my_list:
    set1.add(element)
print(f"第一次添加列表后集合结果为：{set1}")



for element in my_list:
    print(f"列表元素为：{element}")
print("----------------------------")

# 在for 循环中将列表添加至集合
for element in my_list:
    set1.add(element)
print(f"添加列表后集合结果为：{set1}")
print('========================')

