# -- coding: utf-8 --
# @Time: 2021/4/14 17:18
# @Author: Zavijah
# @File: example_2.py
# @Software: PyCharm
# @Purpose:


import numpy as np
import matplotlib.pyplot as plt

a = 2  # 定义a的值  物理意义：波速
l = 5  # 定义l的值

t = np.linspace(0, 10, 100)
x = np.linspace(0, l, 10000)


# 定义函数
def u(x, t):
    temp = (np.cos(np.pi * a * t / l) + 1 / (2 * np.pi * a) * np.sin(2 * np.pi * a * t / l)) * np.sin(np.pi * x / l)
    return temp



plt.figure(figsize=(12, 5))


for i in range(t.size):
    plt.cla()
    plt.title("time = {:.2f}s".format(t[i]))
    plt.ylim(-2, 2)
    plt.xlim(0 - 1, l + 1)

    y = u(x, t[i])

    plt.plot(x, y)

    plt.pause(0.01)

plt.pause(2)
plt.close()
