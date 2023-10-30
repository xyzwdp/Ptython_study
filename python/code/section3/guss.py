"""
1、数字随机产生
2、有3次机会猜测数据，通过3层嵌套来完成
3、每次猜不中，会提示大了或小了
"""

#所产生的随机数两端是闭区间
import random

num=random.randint(1,10)

print(num)

guss_num=int(input("请输入你要猜测的数字："))

if num==guss_num:
    print("恭喜你踩狗屎运了！")
else:
    if guss_num>num:
        print("你猜测数据大咯！")
    else:
        print("你猜测的数据小了！")

    guss_num = int(input("请再次输入你要猜测的数字："))
    if num == guss_num:
        print("恭喜你踩狗屎运了！！")
    else:
        if guss_num > num:
            print("你猜测数据大咯！")
        else:
            print("你猜测的数据小了！")

        guss_num = int(input("请最后输入你要猜测的数字："))
        if num == guss_num:
            print("恭喜你踩狗屎运了！！！")
        else:
            if guss_num > num:
                print("你猜测数据大咯！")
            else:
                print("你猜测的数据小了！")
            print("可惜，游戏结束，你失败了！")