# _*_ coding:UTF-8 _*_
"""
演示json数据何python字典的相互转换
"""
import json

# 准备列表，列表的每个都是字典，将其转换为json
data1 = [{"name": "张三", "age": 15}, {"name": "李四", "age": 16}, {"name": "王五", "age": 17}, ]
json_str1 = json.dumps(data1, ensure_ascii=False)
print(type(json_str1))
print(json_str1)
print('-------------------------')

# 准备列表，见字典转换为json
data2 = {"name": "张三", "age": 15}
json_str2 = json.dumps(data2, ensure_ascii=False)
print(type(json_str2))
print(json_str2)
print('-------------------------')

# 将json字符串转换为python数据类型[{a:b,c:d},{f:g,h:l}]
s = '[{"name": "张三", "age": 15}, {"name": "李四", "age": 16}, {"name": "王五", "age": 17}]'
l=json.loads(s)
print(type(l))
print(l)

# json字符串转换为python数据类型{a:b,c:d}
s = '{"name": "张三", "age": 15}'
d=json.loads(s)
print(type(d))
print(d)
print('---------------------')