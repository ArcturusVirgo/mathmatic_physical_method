# -- coding: utf-8 --
# @Time: 2021/3/19 17:08
# @Author: Zavijah
# @File: example_4.py
# @Software: PyCharm
# @Purpose:


import numpy as np
import matplotlib.pyplot as plt

a = 2  # 定义a的值
t = np.linspace(0, 5, 1000)  # 构造时间序列
x = np.linspace(-20, 20, 1000)  # 构造x


def u(x, t):
    temp = np.sin(x) * np.cos(a * t) + 2 * x * t
    return temp


for i in range(1, t.size):
    plt.clf()
    plt.title("time = {:.2f}s".format(t[i]))
    plt.ylim(-4, 4)
    # plt.xlim(-20, 20)

    y = u(x, t[i])

    plt.plot(x, y)

    plt.pause(0.01)

plt.close()
plt.pause(2)
