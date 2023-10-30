"""
字典常用操作
"""

pay_up_post = {
    "杨叶紫": {
        "部门": "科技部",
        "工资": "3000",
        "级别": "1"},
    "吴书": {
        "部门": "市场部",
        "工资": "5000",
        "级别": "2"},
    "张三": {
        "部门": "市场部",
        "工资": "7000",
        "级别": "3"},
    "李四": {
        "部门": "科技部",
        "工资": "4000",
        "级别": "1"},
    "王五": {
        "部门": "市场部",
        "工资": "6000",
        "级别": "2"}
}

my_dict={2:1}

print(type(my_dict[2]))
# print(f"全体员工当前信息如下：{pay_up_post}")

print(type(pay_up_post["杨叶紫"]["级别"]))

for key1 in pay_up_post:
    # new_dict = pay_up_post[key1]
    # for key2 in new_dict:
        # print(key2)
        # if pay_up_post[key1][key2] == '1':
        if pay_up_post[key1]["级别"] == '1':
            # print(key2)
            pay_up_post[key1]["工资"] = int(pay_up_post[key1]["工资"]) + 1000
            pay_up_post[key1]["级别"] = int(pay_up_post[key1]["级别"]) + 1

print(f"全体员工级别为1的员工升职加薪操作后为：{pay_up_post}")
