"""
列表常用操作
"""
# 定义列表
list_a = [11, 22, 33, "小不点", False]

list_b = [['aa', 'bb', 'cc'], ['wo', 'ai', 'ni']]

# 查找某个元素下标
print(list_a.index("小不点"))
# print(list_b.index(33))
print(list_b.index(['wo', 'ai', 'ni']))
print('-------------------')

# 修改某个指定元素
list_a[0] = '张三'
print(f"列表修改后为：{list_a}")
print('---------------------')

# 指定下标插入元素
list_a.insert(1, '李四')
print("列表插入元素后结果%s", (list_a))
print('-------------------------')

# 在列表尾部追加 单个 心元素
list_a.append(True)
print('列表在列表末尾追加元素后为：%s', (list_a))
print('------------------------')

# 在列表尾部追加 多个 心元素
# list_a.extend(list_b)
# print(f"列表追加一个列表后结果为{list_a}")

#追加容器里的内容
list_a.extend(['wo', 'xi', 'huan', 'diaoyu'])
print(f"列表追加一个列表后结果为{list_a}")

list_c = [11, 22, 33, "小不点", False]
tuple_1=(1,2,3)
list_c.extend(tuple_1)
print(f"list_c列表追加一个列表后结果为{list_c}")
print('---------------------')

# 通过下表删除元素
list_a = [11, 22, 33, "小不点", False]

list_b = [['aa', 'bb', 'cc'], ['wo', 'ai', 'ni']]

del list_a[0]
print(f"删除后列表值为{list_a}")

del list_b[1][2]
print(f"删除后列表值为{list_b}")
print('---------------------')

# 通过下标取出特定元素
ele = list_a.pop(1)
print(f"取出后元素列表为：{list_a}")
print(f'所取出元素为：{ele}')
# 取出嵌套列表元素
ele_1 = list_b.pop(1)[1]
print(f"取出后元素列表为：{list_b}")
print(f'所取出元素为：{ele_1}')
print('-------------------------')

# 通过内容删除元素
list_a = [11, 22, 22, 33, "小不点", False]

list_b = [['aa', 'bb', 'bb', 'cc'], ['wo', 'bb', 'ai', 'ni']]

list_a.remove(22)
print(f"remove删除特定内容后为：{list_a}")

# remove不能删除嵌套列表内层指定元素
# list_b.remove('bb')
# print(f"remove删除特定内容后为：{list_b}")
print('-----------------------')

# 清空列表
list_a.clear()
list_b.clear()
print(f"清空后列表是：{list_a}")
print(f"清空后列表是：{list_b}")
print('-----------------')

# 统计列表中某元素个数
list_a = [11, 22, 22, 33, "小不点", False]

list_b = [['aa', 'bb', 'bb', 'cc'], ['wo', 'bb', 'ai', 'ni']]

count=list_a.count(22)
print(f'元素22在列表list_a中有 {count} 个')
#remove不能统计嵌套列表内层指定元素
count=list_a.count('bb')
print(f'元素22在列表list_b中有 {count} 个')
print('------------------------')

# 统计列表中全部元素数量
list_a = [11, 22, 22, 33, "小不点", False]

list_b= [['aa', 'bb', 'bb', 'cc'], ['wo', 'bb', 'ai', 'ni']]

count1=len(list_a)
print(f"list_a中元素个数有：{count1}")

count2=len(list_b)
print(f"list_b中元素个数有：{count2}")