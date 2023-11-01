"""
参数传递
"""

# 位置参数
def user_info(name,age,gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

user_info('张三',22,'男')
print('==================================')

# 关键参数  关键参数必须在位置参数之后
user_info(age='2',gender='女',name='李四')
user_info('李四',gender='女',age=65)
user_info('李四',age=65,gender='女')
print('==================================')

# 缺省参数，默认参数需写在最后
def user_info(name,age,gender='女'):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

user_info('王五',66)
user_info('王五',66,"男")
print('==================================')

# 不定长参数-位置----*args
# args可以自定义
# 不定长定义的形式参数作为元组存在，接收不定长数量的参数传入

def user_info(*args):
    print(f'不定长位置参数类型是：{type(args)},内容是：{args}')

user_info(1,2,True,"李四",["王",'八','蛋'])
print('--------------------------')

# 不定长---关键字不定长----**号 keywargs
def user_info(**keywargs):
    print(f'不定长位置参数类型是：{type(keywargs)},内容是：{keywargs}')

user_info(name='张三',age=2,var=True)
print('--------------------------')