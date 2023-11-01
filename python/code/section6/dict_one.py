"""
字典学习
"""

#定义字典
my_dict={"测试":10000,"测开":15000,"安全":25000}

#定义空字典
my_dict1={}
my_dict2=dict()
print(f"my_dict的内容是：{my_dict}，类型是：{type(my_dict)}")
print(f"my_dict1的内容是：{my_dict1}，类型是：{type(my_dict1)}")
print(f"my_dict2的内容是：{my_dict2}，类型是：{type(my_dict2)}")
print('======================================')

# 定义重复Key的字典=========键不可以重复，重复会去重，新的会把老的去重，Value可以重复
my_dict3={"测试":10000,"测开":15000,"安全":25000,"安全":25000}
print(f"my_dict3的内容是：{my_dict3}，类型是：{type(my_dict3)}")
my_dict4={"测试":10000,"测开":15000,"安全":25000,"开发":25000}
print(f"my_dict4的内容是：{my_dict4}，类型是：{type(my_dict4)}")
print('======================================')

# 从dict中基于Key获取value
score1=my_dict["测试"]
score2=my_dict["测开"]
score3=my_dict["安全"]
print(f"测试工资为：{score1}")
print(f"测开工资为：{score2}")
print(f"安全工资为：{score3}")
print('--------------------------------------')

# 定义嵌套字典
dict_pay={
    "测试":{"基本工资":4000,
            "加班":4000,
            "奖金":4000
            },
    "测开":{
            "基本工资":7000,
            "加班":6000,
            "奖金":3000
         },
    "安全":{
            "基本工资":10000,
            "加班":8000,
            "奖金":7000
        }

    }

print(f"员工的工资为：{dict_pay}")

# 从嵌套字典中获取信息
pay_dict=dict_pay["安全"]["基本工资"]
print(f"安全的基本工资是：{pay_dict}")
print('-------------------------------------')

# 键值对的Key和Value可以是任意类型（Key不可以是字典）

my_dict={(1,2,3):[1,2,3]}
print(f"键为元组，值为列表的结果为：{my_dict}")
print(my_dict[(1,2,3)])

# my_dict5={{(1,2,3):[1,2,3]}:2222}
# print(my_dict5)