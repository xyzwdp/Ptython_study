"""
元组定义与操作
"""

# # 定义元组
# tuple_1=(1,'hello',True)
# tuple_2=()
# tuple_3=tuple()
#
# print(f'tuple_1的类型是：{type(tuple_1)}，内容是：{tuple_1}')
# print(f'tuple_2的类型是：{type(tuple_2)}，内容是：{tuple_2}')
# print(f'tuple_3的类型是：{type(tuple_3)}，内容是：{tuple_3}')
# print('----------------------')
#
# # 定义单个元素的元组
#
tuple_4=('不是元组')
tuple_5=('单个',)
#
print(f'tuple_4的类型是：{type(tuple_4)}，内容是：{tuple_4}')
print(f'tuple_5的类型是：{type(tuple_5)}，内容是：{tuple_5}')
# print('----------------------')
#
# # 元组的嵌套
#
# tuple_6=(True,(1,2,3),[4,5,6])
# print(f'tuple_6的类型是：{type(tuple_6)}，内容是：{tuple_6}')
# print('----------------------')
#
# # 小标索引取出内容
# tuple_6=(True,(1,2,3),[4,5,6])
# p1=tuple_6[1][1]
# p2=tuple_6[2][2]
#
# print(f'从嵌套元组中取出元素为：{p1}')
# print(f'从嵌套元组中取出元素为：{p2}')
# print('-----------------------')
#
# # 元组的操作，index查找方法
tuple_7=(1,2,4,5,6,1,2,3)
index=tuple_7.index(6)
print(f'元组tuple_7中查找元素2，的下标是：{index}')
# print(tuple_7[-3])
# print('---------------')
#
# # 元组的操作，count统计方法
# tuple_8=(1,2,4,5,6,1,2,3)
# num=tuple_8.count(2)
# print(f'在元组tuple_8中元素 2 的数量有：{num}个')
#
# # len函数统计元组元素数量
# tuple_8=(1,2,4,5,6,1,2,3)
# num=len(tuple_8)
# print(f"元组tuple_8中元素总数为：{num}")
# print('------------------------------')
#
# # 元组遍历：while
index = 0
# def while_t():
#     tuple_8 = (1, 2, 4, 5, 6, 1, 2, 3)
#     while index < len(tuple_8):
#         ele = tuple_8[index]
#         print(ele)
#         # index=index+1
#         index += 1


# while_t()
print('----------------')

# 元组遍历：for
tuple_8 = (1, 2, 4, 5, 6, 1, 2, 3)
for ele in tuple_8:
    print(f"lalala:{ele}")

# 修改元组中列表的内容
tuple_6=(True,(1,2,3),[4,5,6])
print(f'修改前的内容{tuple_6}')
tuple_6[2][1]=6
print(f'修改后的内容{tuple_6}')

del tuple_6[2][1]
print(f'删除后的内容{tuple_6}')

tuple_6[2].append(6666)

print(f'增加后的内容{tuple_6}')

# if __name__ == '__main__':
#     while_t()
#     print("执行")
