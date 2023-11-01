"""
数据容器通用操作
"""

my_list=[1,2,3,4,5]

my_tuple=(1,2,3,4,5)

my_str="abcdefg"

my_set={1,2,3,4,5}

my_dict={'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}

# len统计元素个数
# print(f'列表 元素个数有：{len(my_list)}')
# print(f'元组 元素个数有：{len(my_tuple)}')
# print(f'字符串 元素个数有：{len(my_str)}')
# print(f'集合 元素个数有：{len(my_set)}')
# print(f'字典 元素个数有：{len(my_dict)}')
# print('==============================')

# max统计最大元素
# print(f'列表 最大元素为：{max(my_list)}')
# print(f'元组 最大元素为：{max(my_tuple)}')
# print(f'字符串最大元素为：{max(my_str)}')
# print(f'集合 最大元素为：{max(my_set)}')
# print(f'字典 最大元素为：{max(my_dict)}')
# print('==============================')

# mmin统计最小元素
# print(f'列表 最小元素为：{min(my_list)}')
# print(f'元组 最小元素为：{min(my_tuple)}')
# print(f'字符串最小元素为：{min(my_str)}')
# print(f'集合 最小元素为：{min(my_set)}')
# print(f'字典 最小元素为：{min(my_dict)}')
# print('==============================')

# 类型转换：容器转列表
# print(f"列表转列表的结果是：{list(my_list)}")
# print(f"元组转列表的结果是：{list(my_tuple)}")
# print(f"字符串转列表的结果是：{list(my_str)}")
# print(f"集合转列表的结果是：{list(my_set)}")
# print(f"字典转列表的结果是：{list(my_dict)}")
# print('==============================')

# 类型转换：容器转元组
# print(f"列表转元组的结果是：{tuple(my_list)}")
# print(f"元组转元组的结果是：{tuple(my_tuple)}")
# print(f"字符串元组表的结果是：{tuple(my_str)}")
# print(f"集合转元组的结果是：{tuple(my_set)}")
# print(f"字典转元组的结果是：{tuple(my_dict)}")
# print('==============================')

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串字符串表的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")
print(f"元组的类型是：{type(my_tuple)}")
print('==============================')

# 类型转换：容器转集合
# print(f"列表转集合的结果是：{set(my_list)}")
# print(f"元组转集合的结果是：{set(my_tuple)}")
# print(f"字符串集合表的结果是：{set(my_str)}")
# print(f"集合转集合的结果是：{set(my_set)}")
# print(f"字典转集合的结果是：{set(my_dict)}")
# print('==============================')

# 进行容器的排序
# my_list=[2,3,1,4,5]
#
# my_tuple=(3,2,1,4,5)
#
# my_str="abgfec"
#
# my_set={5,2,3,4,1}
#
# my_dict={'key1':4,'key2':3,'key3':2,'key4':1,'key5':5}
#
# # 正排序
# print(f"列表对象的排序结果是：{sorted(my_list)}")
# print(f"元组对象的排序结果是：{sorted(my_tuple)}")
# print(f"字符串对象的排序结果是：{sorted(my_str)}")
# print(f"集合对象的排序结果是：{sorted(my_set)}")
# print(f"字典对象的排序结果是：{sorted(my_dict)}")
# print('==============================')
#
# # 逆排序
# print(f"列表对象的逆排序结果是：{sorted(my_list, reverse=True)}")
# print(f"元组对象的逆排序结果是：{sorted(my_tuple, reverse=True)}")
# print(f"字符串对象的逆排序结果是：{sorted(my_str, reverse=True)}")
# print(f"集合对象的逆排序结果是：{sorted(my_set, reverse=True)}")
# print(f"字典对象的逆排序结果是：{sorted(my_dict, reverse=True)}")
# print('==============================')