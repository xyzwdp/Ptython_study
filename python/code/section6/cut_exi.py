"""
切片练习
"""
# 输出我想你
# 切片方法
my_str="点不小，你想我，刻无时无"
result1=my_str[6:3:-1]
print(f"真的吗？{result1}")

# 切片取出，然后反转
result2=my_str[4:7][::-1]
print(f"真的吗？{result2}")

# 分割方法split
my_str="点不小，你想我了，刻无时无"
result3=my_str.split("，")
print(f"真的吗？{result3}")
result4=result3[1]
print(type(result4))
print(result4)
result5=result4.replace("了","")
print(result5)
result6=result5[::-1]
print(result6)

result7=my_str.split("，")[1].replace("了","")[::-1]
print(f"真的吗？{result7}")
