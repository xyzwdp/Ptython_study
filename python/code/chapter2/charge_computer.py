"""
计算9天后股价
"""

name="大鹏股份"
stock_price=3.88
stock_code=2222
stock_growth=1.2
growth_day=9

stock_growth_9=1.2**9

print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_growth_9}")

print("公司：%s,公司股票代码是：%d,每日增长系数：%s,经过9天的增长后，股价达到了：%.2f"%(name,stock_code,stock_growth,stock_growth_9))
