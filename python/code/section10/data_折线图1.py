# _*_ coding:UTF-8 _*_
"""
折线图开发
"""
import json
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts,LabelOpts
from pyecharts.charts import Line

# 处理数据
# 美国数据
f_us = open("E:\\test\\python_data\\资料\\第1-12章资料\\资料\\可视化案例数据\\折线图数据\\美国.txt", 'r',
            encoding='UTF-8')
us_data = f_us.read()

# 日本数据
f_jp = open("E:\\test\\python_data\\资料\\第1-12章资料\\资料\\可视化案例数据\\折线图数据\\日本.txt", 'r',
            encoding='UTF-8')
jp_data = f_jp.read()

# 印度数据
f_in = open("E:\\test\\python_data\\资料\\第1-12章资料\\资料\\可视化案例数据\\折线图数据\\印度.txt", 'r',
            encoding='UTF-8')
in_data = f_in.read()

# 去掉不合json规范开头
# 美国
us_data = us_data.replace("jsonp_1629344292311_69436(", '')

# 日本
jp_data = jp_data.replace("jsonp_1629350871167_29498(", '')

# 印度
in_data = in_data.replace("jsonp_1629350745930_63180(", '')

# 去掉不合json规范结尾
# 美国
us_data = us_data[:-2]

# 日本
jp_data = jp_data[:-2]

# 印度
in_data = in_data[:-2]

# json转python字典
# 美国
us_dict = json.loads(us_data)

# 日本
jp_dict = json.loads(jp_data)

# 印度
in_dict = json.loads(in_data)

# print(type(us_dict))
# print(us_dict)

# 获取trend key
# 美国
us_trend_data = us_dict['data'][0]['trend']

# 日本
jp_trend_data = jp_dict['data'][0]['trend']

# 印度
in_trend_data = in_dict['data'][0]['trend']

# print(type(trend_data))
# print(us_trend_data)

# 获取日期数据，用户x轴，取2020年（到315下标结束）
us_x_data = us_trend_data['updateDate'][:314]

jp_x_data = jp_trend_data['updateDate'][:314]

in_x_data = in_trend_data['updateDate'][:314]

# print(us_x_data)

# 获取确诊数据，用户y轴，取2020年到315下标结束
us_y_data = us_trend_data['list'][0]['data'][:314]

jp_y_data = jp_trend_data['list'][0]['data'][:314]

in_y_data = in_trend_data['list'][0]['data'][:314]
# print(us_y_data)

# 生成图表
line = Line()

# 添加x轴数据
line.add_xaxis(us_x_data)

# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data,label_opts=LabelOpts(is_show=False))

# 全局选项设置
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确认人数对比折线图",pos_left="center",pos_bottom="1%"),
    # legend_opts=LegendOpts(is_show=True),
    # toolbox_opts=ToolboxOpts(is_show=True),
    # visualmap_opts=VisualMapOpts(is_show=True)
)

# 调用render方法，生成图表
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()
