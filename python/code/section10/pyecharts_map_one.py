# _*_ coding:UTF-8 _*_
"""
可视化的地图基本使用
"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()

# 准备数据
map_data = [
    ("北京市", 99),
    ("上海市", 19),
    ("湖南省", 9),
    ("贵洲省", 399),
    ("广东省", 99),
    ("安徽省", 699),
    ("湖北省", 499)
]

# 添加数据
map.add("测试地图", map_data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#12562e"},
            {"min":10,"max":99,"label":"10-99","color":"#122f56"},
            {"min":100,"max":800,"label":"100-800","color":"#56122e"}
        ]
    )

)

# 绘图
map.render()
