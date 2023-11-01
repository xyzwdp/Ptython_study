# _*_ coding:UTF-8 _*_
"""
pyecharts基本入门
"""
# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

# 创建一个折现图对象
line=Line()

# 给折线图对象添加x轴数据
line.add_xaxis(["中国","美国","小日子"])
# 给轴线图对象添加y轴数据
line.add_yaxis("GDP",[30,40,5])

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    # title_opts=TitleOpts(title="GDP展示")
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 生成图标
line.render()