"""
函数嵌套调用
"""

def add(a,b):
    result=a+b
    return result

def mul(c,d):
    amass=d*c
    print(f"和的结果是:{add(1,2)}")
    return amass

x=mul(2,3)

print(f"积的结果是:{x}")