# -- coding: utf-8 --
# @Time: 2021/10/3 17:26
# @Author: Zavijah  zavijah@qq.com
# @File: q.py
# @Software: PyCharm
# @Purpose:


import matplotlib.pyplot as plt
import numpy as np

D = np.array([0, 15, 0, 15])
a = 1
Mx = 100
My = 100
T = 5
Nt = 10000
dx = 0.05
dy = 0.05
dt = T / Nt
u0 = 100
u_env = 300
U = u0 * np.ones((My + 1, Mx + 1))
# x方向二阶导系数矩阵A
A = (-2) * np.eye(Mx + 1, k=0) + (1) * np.eye(Mx + 1, k=-1) + (1) * np.eye(Mx + 1, k=1)
# y方向二阶导系数矩阵B
B = (-2) * np.eye(My + 1, k=0) + (1) * np.eye(My + 1, k=-1) + (1) * np.eye(My + 1, k=1)
rx, ry = a * dt / dx ** 2, a * dt / dy ** 2
x = np.linspace(D[0], D[1], U.shape[1])
y = np.linspace(D[2], D[3], U.shape[0])
X, Y = np.meshgrid(x, y)
for k in range(Nt + 1):
    U = U + rx * np.dot(U, A) + ry * np.dot(B, U)
U[:, 0] = U[:, -1] = u_env
U[0, :] = U[-1, :] = u_env
plt.clf()
plt.imshow(U)
plt.show()
