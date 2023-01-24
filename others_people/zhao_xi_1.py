# -- coding: utf-8 --
# @Time: 2021/5/20 23:16
# @Author: Zavijah
# @File: zhao_xi_1.py
# @Software: PyCharm
# @Purpose:

import numpy as np
import matplotlib.pyplot as plt

a = 1
u0 = 0
u1 = 15
u2 = 10
l = 10
x = np.linspace(0, 10, 100)
t = np.linspace(0, 10, 100)


def u(x,t):
    for i in range(1,100000):
        j=1
        tem1=(u1-u0)*(pow((-1),j)-1)/(j*np.pi)+(u2-u1)*pow((-1),j)/(j*np.pi) \
        *np.exp(-1*(j**2) *(np.pi**2)*a^2 *t/ l^2)*np.sin(i*np.pi*x/l)
        j=j+1
    tem2=u1+(u2-u1)*x/l+2*tem1
    return tem2



for k in range(t.size):
    plt.cla()
    fig = plt.axes(projection='3d')
    z = u(x, t)
    fig.plot_wireframe(x, t, u(x, t), color='red')
    fig.set_xlabel('X')
    fig.set_ylabel('T')
    fig.set_zlabel('U')
    plt.pause(0.1)
plt.pause(2)
plt.show()
plt.close()
