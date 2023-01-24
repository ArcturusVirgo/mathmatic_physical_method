# -- coding: utf-8 --
# @Time: 2021/5/17 22:26
# @Author: Zavijah
# @File: demo_1.py
# @Software: PyCharm
# @Purpose:
# 求解热传导方程
# $$
# \begin{cases}
# 	u_t-a^2u_{xx}=0\\
# 	u\left( 0,t \right) =u\left( l,t \right) =0\\
# 	u\left( x,0 \right) =\varphi \left( x \right)\\
# \end{cases}
# $$
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sym


plt.rcParams['font.family'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False  # 负号显示的相关设置

l = 5  # 杆的长度
a = 1

t = np.linspace(0, 5, 100)  # 时间序列
x = np.linspace(0, l, 1000)  # 坐标空间


# 定义函数
def u(x, t):
    result = np.zeros(x.size)

    def phi(x):  # phi函数
        temp_1 = 100
        return temp_1

    def cn_pre(n):  # 系数, sym库的积分
        x = sym.symbols("x")
        temp_2 = sym.integrate(phi(x) * sym.sin(n * np.pi / l * x), (x, 0, l)) * 2 / l
        return temp_2

    def cn_num(n):  # 系数, sci库的积分
        temp_2 = quad(lambda x: (phi(x) * np.sin(n * np.pi * x / l)), 0, l)[0] * 2 / l
        return temp_2

    for n in range(1, 50):  # 累加求和
        result = result + cn_num(n) * np.exp(-(n * np.pi * a / l) ** 2 * t) * np.sin(n * np.pi * x / l)
    return result


fig = plt.figure(figsize=(12, 4))
for i in range(t.size):  # 循环变时间
    plt.clf()  # 清除窗口内容
    plt.title("杆的热传导问题\nt = {:.2f}".format(t[i]))  # 设置窗口标题

    value = u(x, t[i])  # 计算函数值
    value = value.astype(np.float64)
    print(value.max(), value.min())

    # 画法1
    # plt.ylim(0, 117)  # 设置y轴范围
    # plt.ylabel("温度")  # 设置纵轴标签
    # plt.xlabel("位置坐标")  # 设置横轴标签
    # plt.plot(x, value)  # 画图

    # # 画法2
    value = np.vstack((value, value))
    plt.yticks([])  # 不显示y轴刻度
    plt.xlabel("位置坐标")  # 设置横轴标签
    plt.imshow(value, cmap='jet', vmin=0, vmax=117, origin="lower", extent=[0, l, 0, l / 12])  # 画图
    position = fig.add_axes([0.15, 0.2, 0.7, 0.05])  # 颜色条位置[x, y, width, height]
    plt.colorbar(cax=position, orientation='horizontal')  # 设置颜色条

    # plt.pause(10)
    plt.pause(0.01)  # 暂停 0.01s

plt.pause(10)  # 画完后暂停10s
