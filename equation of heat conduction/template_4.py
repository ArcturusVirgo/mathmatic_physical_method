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

a = 1
l = 1
x = np.linspace(0, l, 100)
t = np.linspace(0, 1, 100)
X, T = np.meshgrid(x, t)


def u(x, t):
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

    result = cn_num(1) * np.exp(-(1 * np.pi * a / l) ** 2 * t) * np.sin(1 * np.pi * x / l)
    for n in range(2, 50):  # 累加求和
        result = result + cn_num(n) * np.exp(-(n * np.pi * a / l) ** 2 * t) * np.sin(n * np.pi * x / l)
    return result


z = u(X, T)


fig = plt.figure(figsize=(8, 6))

for i in range(t.size):
    plt.clf()

    ax1 = fig.add_subplot(221)
    value = z[i, :]
    plt.ylim(z.min(), z.max())  # 设置y轴范围
    plt.ylabel("温度")  # 设置纵轴标签
    plt.xlabel("位置坐标")  # 设置横轴标签
    plt.plot(x, value)  # 画图

    ax2 = fig.add_subplot(222, projection='3d')
    ax2.set_xlabel("X")
    ax2.set_ylabel("T")
    ax2.set_zlabel("U")
    ax2.view_init(elev=10, azim=60)
    ax2.plot_surface(X, T, z, cmap="jet")

    ax3 = fig.add_subplot(212)
    plt.title("杆的热传导问题\nt = {:.2f}".format(t[i]))  # 设置窗口标题
    value = np.vstack((value, value))
    plt.yticks([])  # 不显示y轴刻度
    plt.xlabel("位置坐标")  # 设置横轴标签
    plt.imshow(value, cmap='jet', vmin=z.min(), vmax=z.max(), extent=[0, l, 0, l / 10])  # 画图
    position = fig.add_axes([0.15, 0.1, 0.7, 0.03])  # 颜色条位置[x, y, width, height]
    plt.colorbar(cax=position, orientation='horizontal')  # 设置颜色条

    plt.pause(0.01)  # 暂停 0.01s
plt.pause(10)  # 画完后暂停10s
