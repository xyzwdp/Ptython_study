# _*_ coding:UTF-8 _*_
"""
演示河南省疫情地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据
f_hn = open("E:\\test\\python_data\\资料\\第1-12章资料\\资料\\可视化案例数据\\地图数据\\疫情.txt", 'r',
            encoding='UTF-8')
epi_data = f_hn.read()

# 关闭文件
f_hn.close()

# 准备数据为元组放入list
hn_dict=json.loads(epi_data)

# 获取河南省数据
hn_data_list=hn_dict["areaTree"][0]["children"][3]["children"]

# 组装每个市确诊人数为元组，并将各个市的数据都封装如列表内
data_list=[]
for city_data in hn_data_list:
    city_name=city_data["name"]+"市"
    # city_name=city_name.replace(city_name,city_name+"市")
    city_confirm=city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm))

data_list.append(("济源市",5))
# 构建地图
map=Map()

# 添加数据
map.add("河南省疫情数据",data_list,"河南")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南疫情地图"),
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
map.render("河南省疫情地图.html")
