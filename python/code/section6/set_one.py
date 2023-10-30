"""
set定义
"""

#定义set
my_set1={"测开","月薪过万","地点广州","测开","月薪过万","地点广州","测开","月薪过万","地点广州"}
my_set2=set()
my_set3={"测开","月薪过万","地点广州","测开","月薪过万","地点广州"}

print(f"my_set1的内容是：{my_set1}，类型是：{type(my_set1)}")
print(f"my_set2的内容是：{my_set2}，类型是：{type(my_set2)}")
print(f"my_set3的内容是：{my_set3}，类型是：{type(my_set3)}")
print("----------------------------")

# set添加新元素---add
my_set3.add("python")
my_set3.add("侧开")
print(f"my_set3添加元素后结果：{my_set3}")
print("----------------------------")

# set移除元素---remove
my_set3.remove("地点广州")
# 不能移除不存在的元素
# my_set3.remove("地点广")
print(f"my_set3移除元素后结果：{my_set3}")
print("----------------------------")

# 随机取出元素---pop，不能去指定元素
my_set3={"测开","月薪过万","地点广州","测开","月薪过万","地点广州"}
result1=my_set3.pop()
print(result1)
print(my_set3)
print("----------------------------")

# 清空集合---clear
my_set3.clear()
print(f"清空集合结果为：{my_set3}")
print("----------------------------")

# 取两个集合的差集---difference
set1={1,2,3}
set2={1,3,5}
set4={1,2,3}
set3=set1.difference(set2)
set5=set1.difference(set4)
print(f"取出set1比set2的差集结果为：{set3}")
print(f"取出差集后，set1的结果为：{set1}")
print(f"取出差集后，set2的结果为：{set2}")
print(f"取出set1比set4的差集结果为：{set5}")
print("------------------------")

# 消除差集---difference_update
set1={1,2,3}
set2={1,3,5}
set3=set1.difference_update(set2)
print(f"消除set1比set2的差集结果为：{set3}")
print(f"消除差集后，set1的结果为：{set1}")
print(f"消除差集后，set2的结果为：{set2}")
print("------------------------")

# 集合合并---union
set1={1,2,3}
set2={1,3,5}
set3=set1.union(set2)
print(f"set1与set2合并后结果为：{set3}")
print(f"合并集后后，set1的结果为：{set1}")
print(f"合并集合后，set2的结果为：{set2}")
print("------------------------")

# 统计元素数量----len()
set1={1,2,3}
set2={1,2,3,1,2,3}
num=len(set1)
num1=len(set2)

print(f"set1集合内的元素数量有：{num}个")
print(f"set2集合内的元素数量有：{num1}个")
print("------------------------")

# 集合遍历
# 集合不支持小标索引，不能用while循环
#可以用for 循环遍历
set1={1,2,3}
for element in set1:
    print(f"set1集合元素有：{element}")