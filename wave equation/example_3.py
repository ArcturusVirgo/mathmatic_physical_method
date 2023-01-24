# -- coding: utf-8 --
# @Time: 2021/4/14 17:18
# @Author: Zavijah
# @File: example_3.py
# @Software: PyCharm
# @Purpose:


import numpy as np
import matplotlib.pyplot as plt

a = 2  # 定义a的值  物理意义：波速
l = 5  # 定义l的值

t = np.linspace(0, 10, 1000)
x = np.linspace(0, 5, 1000)

# 定义函数
def u(x, t):
    # 将最终解的表达式写在这里
    temp = 2 * np.cos(2 * np.pi * a * t / l) * np.cos(2 * np.pi * x / l)
    # “\”表示代码换行
    # numpy中各种函数的用法见 numpy.html 文件（在群里）
    return temp  # 将计算出的函数值返回

# 构建画布，大小为1200px*500px
plt.figure(figsize=(12, 5))

# 循环变时间， t.size表示时间序列 t 的长度
for i in range(t.size):
    plt.cla()  # 清除画布内容
    plt.title("time = {:.2f}s".format(t[i]))  # 绘制画布标题，这里绘制为 当前时间
    plt.ylim(-3, 3)
    plt.xlim(0 - 1, l + 1)

    y = u(x, t[i])  # 计算 y 的值

    plt.plot(x, y)  # 画y-x图像

    plt.pause(0.01)  # 暂停 0.01s

plt.pause(2)  # 循环完毕后暂停 2s
plt.close()  # 关闭窗口
