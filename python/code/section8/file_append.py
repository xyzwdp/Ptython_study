"""
文件追加
"""

# 打卡文件，不存在文件
# f=open("E:\\python\\docunmentation\\append.txt",'a',encoding='UTF-8')


# write写入
# f.write("年薪百万")
# flush刷新
# f.flush()

#close关闭
# f.close()

# 打开一个存在文件
f=open("E:\\python\\docunmentation\\append.txt",'a',encoding='UTF-8')

# write写入，flush刷新
f.write("\n继续学习")

# close关闭
f.close()
