# -*- coding: utf-8 -*-#
# ---------------------------
# Author:       STU
# Create Date:  2021/5/7 13:46
# Description:  利用蒙特·卡罗法计算圆周率的近似值
# ---------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 投点次数
n = 5000

# 圆的信息
r = 1.0     # 半径
a, b = (0., 0.)     # 圆心

# 正方形的区域边界
x_min, x_max = a - r, a + r
y_min, y_max = b - r, b + r

# 在正方形区域内随机投点
x = np.random.uniform(x_min, x_max, n)      # 均匀分布
y = np.random.uniform(y_min, y_max, n)

# 计算 点到圆心的距离（sqrt函数是求算数平均值）
d = np.sqrt((x - a) ** 2 + (y - b) ** 2)

# 统计 落在圆内的点的数目
s = np.where(d <= r, 1, 0)      # 圆心距小于等于圆半径
result = sum(s)

# 计算 π 的近似值（用统计值去除近似真实值）
pi = 4 * result / n
print('π的值为：', pi)

# 画图比较耗费时间
fig = plt.figure()      # Figure:画图
axes = fig.add_subplot(111)     # axes:坐标轴（实际画图的地方）
axes.set_title('PI is : %f' % pi)

for i in range(len(s)):
    if s[i] == 1:
        axes.plot(x[i], y[i], 'ro', markersize=2, color='red')      # 园内红色
    else:
        axes.plot(x[i], y[i], 'ro', markersize=2, color='yellow')      # 园外黄色

plt.axis('equal')        # 防止图像变形
circle = Circle(xy=(a, b), radius=r, alpha=0.5)     # alpha：透明度
axes.add_patch(circle)      # add_patch（circle）：添加圆形
plt.show()             # 展示所形成的图形界面
