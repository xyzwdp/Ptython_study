"""
切片学习
"""

# 对list进行切片，从1开始，4结束，步长1
my_list=[0,1,2,3,4,5,6]
result1=my_list[1:4]
print(f"result1切片结果为{result1}")
print('-------------------------')

# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:]
print(f"result2切片结果为{result2}")
print('-------------------------')

# 对str进行切片，从头开始，到最后结束，步长为2
my_str="0123456789"
result3=my_str[::2]
print(f"result3切片结果为{result3}")
print('-------------------------')

# 对str进行切片，从头开始，到最后结束，步长为-1
my_str="0123456789"
result4=my_str[::-1]
print(f"result4切片结果为{result4}")
print('-------------------------')

#对list进行切片，从3开始，到1结束，步长-1
my_list=[0,1,2,3,4,5,6]
result5=my_list[3:1:-1]
print(f"result5切片结果为{result5}")
print('-------------------------')

# 对tuple进行切片，从头开始，到最后结束，步长-2
my_tuple=(0,1,2,3,4,5,6)
result6=my_tuple[::-2]
print(f"result6切片结果为{result6}")
print('-------------------------')
