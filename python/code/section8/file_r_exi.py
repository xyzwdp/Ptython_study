"""
文件读取练习
"""

with open("E:\\python\\docunmentation\\word.txt", "r", encoding="UTF-8") as f:
    count = 0
    for line in f:
        # line.strip()
        # print(line)
        my_list = line.strip().split(" ")
        # print(my_list)
        for i in my_list:
            # print(i)
            if i == "aaaa":
                count += 1
        # print(j)
    print(f"字符串 aaaa 在word文件中出现次数为：{count}")

f=open("E:\\python\\docunmentation\\word.txt", "r", encoding="UTF-8")
content=f.read()
count=content.count('aaaa')
print(f"字符串 aaaa 在word文件中出现次数为：{count}")
f.close()