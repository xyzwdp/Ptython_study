# _*_ coding:UTF-8 _*_
"""
时间柱状图演示
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 创建柱状图对象
bar1=Bar()

bar1.add_xaxis(["中国","美国","英国"])

bar1.add_yaxis("GDP",[80,50,30],label_opts=LabelOpts(position="right"))

bar1.reversal_axis()

bar2=Bar()

bar2.add_xaxis(["中国","美国","英国"])

bar2.add_yaxis("GDP",[100,70,40],label_opts=LabelOpts(position="right"))

bar2.reversal_axis()

bar3=Bar()

bar3.add_xaxis(["中国","美国","英国"])

bar3.add_yaxis("GDP",[150,90,70],label_opts=LabelOpts(position="right"))

bar3.reversal_axis()

# 构建时间线对象
# 主题设置
time_line=Timeline({"theme":ThemeType.LIGHT})

# 在时间线内添加柱状图对象
time_line.add(bar1,"点1")
time_line.add(bar2,"点2")
time_line.add(bar3,"点3")

# 自动播放设置
time_line.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)


# 绘图
# 绘图是用时间线对象绘图，而不是bar对象了
time_line.render("基础时间线柱状图.html")

