# -- coding: utf-8 --
# @Time: 2021/3/30 18:02
# @Author: Zavijah
# @File: example_1.py
# @Software: PyCharm
# @Purpose:
# 求解一维波动问题
# $$
# \begin{cases}
# 	u_{tt}-a^2u_{xx}=0\\
# 	u\left( 0,t \right) =u\left( l,t \right) =0\\
# 	u\left( x,0 \right) =\sin \frac{\pi}{l}x\,\,   u_t\left( x,0 \right) =\sin \frac{2\pi}{l}x\\
# \end{cases}
# \\
# u\left( x,t \right) =\cos \frac{\pi at}{l}\sin \frac{\pi x}{l}+\frac{l}{2\pi a}\sin \frac{2\pi at}{l}\sin \frac{2\pi x}{l}
# $$



import numpy as np
import matplotlib.pyplot as plt

a = 1 # 定 义a的值  物理意义：波速
l = 6  # 定义l的值

t = np.linspace(0, 10, 100)
# 构造时间序列，起始点为0s， 终止为10s，将0到10秒等分为一个列表
# 可使用print()语句查看具体内容

x = np.linspace(0, 6, 10000)
# 构造x，坐标范围为（-10，10）。将这段区间分为10000份，份数越多图像越光滑
# 同时这个区间是画图范围。在（-10， 10）内画图

# 定义函数
def u(x, t):
    temp = np.cos(np.pi * a * t / l) * np.sin(np.pi * x / l) + \
           l / (2 * np.pi * a) * np.sin(2 * np.pi * a * t / l) * np.sin(2 * np.pi * x / l)
    return temp


# 构建画布，大小为1200px*500px
plt.figure(figsize=(12, 5))

# 循环变时间， t.size表示时间序列 t 的长度
for i in range(t.size):
    plt.cla()  # 清除画布内容
    plt.title("time = {:.2f}s".format(t[i]))  # 绘制画布标题，这里绘制为 当前时间
    plt.ylim(-2, 2)  # 设置纵轴坐标轴范围
    plt.xlim(0,6)  # 设置横轴坐标轴范围

    y = u(x, t[i])  # 计算 y 的值

    plt.plot(x, y)  # 画y-x图像

    # plt.pause(10)  # 暂停 0.01s
    plt.pause(0.01)  # 暂停 0.01s

plt.pause(2)  # 循环完毕后暂停 2s
plt.close()  # 关闭窗口

