# _*_ coding:UTF-8 _*_
"""
演示基础树状图的开发
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar构建基础柱状图
bar=Bar()

# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
bar.add_yaxis("GDP",[80,50,30],label_opts=LabelOpts(position="right"))

# 反转xy轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")
# 反转x轴和y轴

# 设置数值标签在右侧