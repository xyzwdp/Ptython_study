"""
写入操作
"""
import time

# 打开文件，不存在文件
# Python文件执行完成，会自动关闭文件
# f=open("E:\\python\\docunmentation\\write.txt",'w',encoding="UTF-8")

# write写入
# f.write("Hello Word")

# flush刷新
# f.flush()
# time.sleep(5000)

# close关闭文件
# f.close()

# 打开一个存在文件
f=open("E:\\python\\docunmentation\\write.txt",'w',encoding="UTF-8")
# write写入，flush刷新
f.write("我要上天")

# close关闭
f.close()