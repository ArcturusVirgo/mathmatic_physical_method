# -- coding: utf-8 --
# @Time: 2021/5/22 23:24
# @Author: Zavijah
# @File: template_2.py
# @Software: PyCharm
# @Purpose:

# 数值法解稳定场方程(矩形域上)

import numpy as np
import matplotlib.pyplot as plt

a = np.pi
b = np.pi
d = 0.05

Nx = int(a / d)
Ny = int(b / d)

x = np.linspace(0, a, Nx + 1)
y = np.linspace(0, b, Ny + 1)
X, Y = np.meshgrid(x, y)

U = np.zeros([Nx + 1, Ny + 1])

temp = 0
for i in range(1, Nx):
    U[i, 0] = np.pi * np.sin(i * d)
    U[i, Ny] = np.pi * np.cos(i * d)
    temp += U[i, Ny] + U[i, 0]
for j in range(1, Ny):
    U[0, j] = j * d
    U[Nx, j] = j * d
    temp += U[0, j] + U[Nx, j]
average = temp / (2 * (Nx + Ny - 2))

for i in range(1, Nx):
    for j in range(1, Ny):
        U[i, j] = average

while True:
    U_initial = U.copy()
    U_temp = U.copy()
    for i in range(1, Nx):
        for j in range(1, Ny):
            U_temp[i, j] = 1 / 4 * (U[i + 1, j] + U[i - 1, j] + U[i, j + 1] + U[i, j - 1])
            U[i, j] = 1 / 4 * (U[i + 1, j] + U_temp[i - 1, j] + U[i, j + 1] + U_temp[i, j - 1])
    if np.abs(U_initial - U).max() < 0.001:
        break

U = U.T

fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(121)
plt.xlabel("X")
plt.ylabel("Y")
# plt.xticks([])
# plt.yticks([])
plt.imshow(U, cmap="jet", origin="lower", extent=[0, a, 0, b])
plt.colorbar()

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("U")
ax2.view_init(elev=10, azim=-30)
ax2.plot_surface(X, Y, U, cmap="jet")

plt.show()
