"""
练习案例：友工资
某公司，账户余额有1W元，给20名员工发工资。
    员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
    领工资时，财务判断员工的绩效分（1—10） （随机生成），如果低于5，不发工资，换下一位如果工资发完了，结束发工资。
    工资发完了，结束发工资
"""
import random

pay_monney = 10000

for i in range(1,21):
    j = random.randint(1, 10)
    print(f"{i}号员工绩效为：{j}")
    if j < 5:
        print(f"员工{i},绩效为{j},低于5，不发工资，下一位")
        i += 1
        print("----------------------")
        continue
    salary = int(1000 * (j/10))
    pay_monney = int(pay_monney - salary)
    if pay_monney > 0:
        print(f"{i}号员工工资是：{salary}")
        print(f"当前所结余工资为：{pay_monney}")
    else:
        print(pay_monney)
        salary = salary + pay_monney
        print(f"{i}号员工工资是：{salary}")
        break
    print("---------------------------")
    i += 1

if pay_monney <= 0:
    print(f"本月结余工资金额为：0")
else:
    print(f"本月结余工资金额：{pay_monney}")
