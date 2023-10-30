# _*_ coding:UTF-8 _*_
"""
全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f_na = open("E:\\test\\python_data\\资料\\第1-12章资料\\资料\\可视化案例数据\\地图数据\\疫情.txt", 'r',
            encoding='UTF-8')
epi_data = f_na.read()

# 关闭文件
f_na.close()

# 取各省数据

# 将字符串json转换为python的字典
data_dict = json.loads(epi_data)

# 从字典中取各省的数据
province_data_list = data_dict['areaTree'][0]["children"]
# print(province_data_list)

# 组装每个省份何确诊人数为元组，并将各个省的数据都封装如列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    # print(type(province_name))
    province_name=province_name.replace(province_name,province_name+"省")
    # province_name_list=list(province_name)
    # province_name_list.append("省")

    # province_name=str(province_name_list)
    # print(province_name)
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

# print(data_list)
# 创建地图对象
map=Map()

# 添加数据
map.add("各省份确诊人数",data_list,"china")

# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        #是否显示
        is_show=True,
        # 是否分段
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"lable":"1-99","color":"#CCFFFF"},
            {"min":100,"max":999,"lable":"100-999","color":"#FFFF99"},
            {"min":1000,"max":4999,"lable":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"lable":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"lable":"10000-99999","color":"#CC3333"},
            {"min":100000,"lable":"100000+","color":"#990033"}
        ]
    )
)

# 绘图
map.render("全国疫情地图.html")
