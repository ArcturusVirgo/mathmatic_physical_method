# -- coding: utf-8 --
# @Time: 2021/5/20 13:14
# @Author: Zavijah
# @File: template_1.py
# @Software: PyCharm
# @Purpose:
# 无界区域的齐次波动问题(达朗贝尔公式)
# $$
# \begin{cases}
# 	u_{tt}-a^2u_{xx}=0\\
# 	u\left( x,0 \right) =\varphi \left( x \right) \,\,   u_t\left( x,0 \right) =\psi \left( x \right)\\
# \end{cases}
# \\
# u\left( x,t \right) =\frac{1}{2}\left[ \varphi \left( x-at \right) +\varphi \left( x+at \right) \right] +\frac{1}{2a}\int_{x-at}^{x+at}{\psi \left( x \right) dx}
# $$

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

plt.rcParams['font.family'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False  # 负号显示的相关设置

l = 10
a = 1

t = np.linspace(0, 10, 100)
x = np.linspace(-l, l, 1000)

# 定义函数
def u(x, t):
    result = np.zeros(x.size)
    def phi(z):
        temp = np.sin(np.pi * z / l)
        return temp

    def psi(z):
        temp = np.sin(2 * np.pi * z / l)
        return temp
    for i in range(x.size):
        result[i] = (phi(x[i]-a*t) + phi(x[i]+a*t)) / 2 + quad(psi, x[i]+a*t, x[i]-a*t)[0] / (2 * a)
    return result

plt.figure(figsize=(12, 5))
for v in t:
    plt.cla()  # 清除画布内容
    plt.title("time = {:.2f}s".format(v))  # 绘制画布标题，这里绘制为 当前时间
    plt.ylim(-2, 2)  # 设置纵轴坐标轴范围
    plt.xlim(- l - 2, l + 2)  # 设置横轴坐标轴范围

    y = u(x, v)  # 计算 y 的值

    plt.plot(x, y)  # 画y-x图像

    plt.pause(0.01)  # 暂停 0.01s

plt.pause(2)  # 循环完毕后暂停 2s
plt.close()  # 关闭窗口