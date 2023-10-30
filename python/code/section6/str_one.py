"""
字符串演示
"""

# my_str="wo xi huan ni"
#
# # 通过下标索引取值
# value1=my_str[3]
# value2=my_str[-10]
# print(f'从字符串my_str取值为：{value1}')
# print(f'从字符串my_str取值为：{value2}')
#
# #字符串不支持修改
# # my_str[2]="n"
#
# # index方法
# value3=my_str.index('xi')
# print(f'在字符串{my_str}中查找and，起始下标是：{value3}')
# print('----------------------')
#
# # replace方法
# n_str=my_str
# print(id(n_str))
# print(id(my_str))
# new_str=my_str.replace('wo','ni')
# print(id(new_str))
# print(id(my_str))
# print(f"将字符串{my_str}进行替换后得到：{new_str}")
# print('--------------------')
#
# # split方法，将字符串进行切分，可以转为列表
# my_str="wo xi huan ni"
# my_str_list=my_str.split(" ")
# print(f'将字符串{my_str}进行split切分后得到：{my_str_list}，类型是：{type(my_str_list)}')
# print('-----------------------------')
#
# #stip方法，整理字符串
# #取出前后空格胡回车符
# # 语法
# # 	字符串.strip()
# # 	去掉前后空格与回车符
my_str=" wo xi " \
       "huan ni  "

new_str=my_str.strip()
print(f"字符串{my_str}被srip后，结果：{new_str}")

# 语法
# 	字符串.strip()
# 	去掉前后指定字符串
my_str="wo xi wo huan ni wo"
new_str1=my_str.strip('xi4')
print(f"字符串{my_str}被srip后，结果：{new_str1}")
print('----------------------')

# 统计字符串中某个字符串出现次数
my_str="wo xi wo huan ni wo"

count1=my_str.count('w')
count2=my_str.count('wo')
count3=my_str.count('ow')

print(f'字符串{my_str}中w出现次数是：{count1}')
print(f'字符串{my_str}中wo出现次数是：{count2}')
print(f'字符串{my_str}中ow出现次数是：{count3}')

# 统计字符串的长度
my_str="wo xi wo huan ni wo"
len_str=len(my_str)
print(f"字符串{my_str}的长度为：{len_str}")

