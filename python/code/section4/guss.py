"""
设置一个范围1-100的随机数，通过while语句，配合input()语句，判断输入的数字是否等于随机数
1、无限次机会，知道猜中为止
2、每一次猜不中，会提示大了或小了
3、猜完数字后，提示猜了几次
"""
import random

num = random.randint(1, 100)
i = 0
print(num)

con = True
while con:
    i += 1
    guss_num = int(input(f"请第{i}次输入你猜的答案："))
    if guss_num == num:
        print()
        print("恭喜你，猜对了，就是数字 %d 天选之子！！！" % num)
        print("你只用了%s次就猜中了，太厉害了！！！" % i)
#        continue
        break
#        con = False
    elif guss_num > num:
        print("很可惜，你猜大了，继续努力！")
    elif guss_num < num:
        print("差一点点哦，你猜小了！！！")
    print("结束了")
