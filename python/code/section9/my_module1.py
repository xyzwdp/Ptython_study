# _*_ coding:UTF-8 _*_
"""
定义被调用的python模块
"""

# 定义函数
def test(a,b):
    print(a+b)

print("__name__:",__name__)

if __name__ == '__main__':
    test(2,3)
