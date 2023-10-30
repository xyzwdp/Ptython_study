count = 0

content = "xyzxyzyxxyzyxyz"

for i in content:
    if i == "x":
        count += 1

print(f"被统计的字符串中有{count}个a")
