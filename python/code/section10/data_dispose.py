# _*_ coding:UTF-8 _*_
"""
演示第三个图标：GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
with open("E:\\test\\python_data\\资料\\第1-12章资料\\资料\\可视化案例数据\\动态柱状图数据\\1960-2019全球GDP数据.csv",
          'r', encoding='GB18030') as f_gdp:
    data_lines = f_gdp.readlines()
# 关闭文件

# 删除第一条数据
data_lines.pop(0)

# 将数据转换为字典存储，格式为：
# {年份:[国家，gdp]}
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 如何判断字典里面有没有指定的key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)
# 排序年份
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)

# 创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})

# for循环每一年的数据，基于每一年的数据，创建每一年bar对象
# 在for中，将每一年的bar对象添加到时间线中
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8的国家
    year_data = data_dict[year][0:8]
    # print(year_data)
    x_data = []
    y_data = []
    for country_gdp in year_data:
        # 添加x轴数据
        # print(country_gdp)
        # print(type(country_gdp))
        # country_gdp[1]=int(country_gdp[1] / 100000000)
        x_data.append(country_gdp[0])
        # 添加y轴数据
        y_data.append(country_gdp[1]/ 100000000)

    # 构建柱状图对象
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar.reversal_axis()
    #设置每一年图标标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 绘图
timeline.render("1960-2019全球GDP前8国家排名.html")
