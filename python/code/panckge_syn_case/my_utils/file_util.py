# _*_ coding:UTF-8 _*_
def print_file_info(file_name):
    """
    查看文件是否存在
    :param file_name:
    :return:
    """
    f=None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        cotent=f.read()
    except Exception as e:
        print(f"程序出异常了，原因是：{e}")
        f = open(file_name, "w", encoding="UTF-8")
        f.write("aaasf")
    else:
        print(cotent)
    finally:
        # 如果变量是None，表示False，如果有任何内容，就是True
        if f:
            f.close()


def append_file_info(file_name,data):
    """
    将指定的数据加导指定的文件中
    :param file_name:指定的文件路径
    :param data:指定的数据
    :return:None
    """
    with open(file_name,'a',encoding="UTF-8") as f:
        f.write(data)
        f.write("\n")
        # print(f.read())

if __name__ == '__main__':
    # print_file_info("E:\\test\python\\python\\docunmentation\\test3.txt")
    append_file_info("E:\\test\python\\python\\docunmentation\\test2.txt","涨薪1万")
