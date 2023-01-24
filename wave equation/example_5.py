# -- coding: utf-8 --
# @Time: 2021/3/30 18:02
# @Author: Zavijah
# @File: 第9题.py
# @Software: PyCharm
# @Purpose:


import numpy as np
import matplotlib.pyplot as plt

a = 10  # 定义a的值
# temp_1
t = np.linspace(0, 10, 1000)  # 构造时间序列
x = np.linspace(-20, 20, 10000)  # 构造x
# temp_2
# t = np.linspace(0, 1, 1000)  # 构造时间序列
# x = np.linspace(-5, 5, 10000)  # 构造x


def u(x, t):
    temp_1 = (1 / (1 + 8 * (x + a * t) ** 2) + 1 / (1 + 8 * (x - a * t) ** 2)) / 2
    temp_2 = (1 / (np.cos(x + a * t) ** 2) + 1 / (np.cos(x - a * t) ** 2)) / 2
    return temp_1


plt.figure(figsize=(12, 5))

for i in range(1, t.size):
    plt.cla()
    plt.title("time = {:.2f}s".format(t[i]))

    # temp_1
    # plt.ylim(0, 100)
    # plt.xlim(-10, 10)

    # temp_2
    plt.ylim(0, 1)
    # plt.xlim(-20, 20)

    y = u(x, t[i])

    plt.plot(x, y)

    plt.pause(0.01)

plt.pause(2)
plt.close()


