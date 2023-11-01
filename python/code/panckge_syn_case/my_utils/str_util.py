# _*_ coding:UTF-8 _*_
def str_reverse(s):
    """
    功能是将字符串反转
    :param s: 将反转的字符串
    :return: 反转后的字符串
    """
    # i = len(s)-1
    # reverse = ""
    # while i >= 0:
    #     reverse = reverse + s[i]
    #     i -= 1
    # print(reverse)
    return s[::-1]

def substr(s,x,y):
    """
    功能是按照给定的下表完成给定字符串切片
    :param s: 将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    result=s[x:y]
    return result


if __name__ == '__main__':
    print(str_reverse("asdfghjkl"))
    # print(substr("123456",2,5))
