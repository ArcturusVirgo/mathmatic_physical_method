# -- coding: utf-8 --
# @Time: 2021/5/21 23:00
# @Author: Zavijah
# @File: template_1.py
# @Software: PyCharm
# @Purpose:
# 解稳定场方程
# $$
# \begin{cases}
# 	\varDelta u=0\\
# 	u\left( 0,y \right) =u\left( a,y \right) =0\\
# 	u\left( x,0 \right) =u_0\,\,\underset{y\rightarrow \infty}{\lim}u\left( x,y \right) =0\\
# \end{cases}
# \\
# u\left( x,y \right) =\sum_{n=1}^{\infty}{B_ne^{-\frac{n\pi}{a}y}\sin \frac{n\pi}{a}x}
# \\
# B_n=\frac{2}{a}\int_0^a{u_0\sin \frac{n\pi}{a}xdx}
# $$

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

u0 = 10
a = 1
x = np.linspace(0, 1, 500)
y = np.linspace(0, 1, 500)
X, Y = np.meshgrid(x, y)


def u(x, y):
    def bn(n):
        temp = quad(lambda x: u0 * np.sin(n * np.pi * x / a), 0, a)[0] * 2 / a
        return temp

    result = bn(1) * np.exp(-np.pi * y / a) * np.sin(np.pi * x / a)
    for n in range(2, 200):
        result = result + bn(n) * np.exp(-n * np.pi * y / a) * np.sin(n * np.pi * x / a)
    return result


z = u(X, Y)
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
plt.xlabel("X")
plt.ylabel("Y")
plt.imshow(z, cmap="jet", origin="lower", extent=[0, a, 0, a])
plt.colorbar()

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("U")
ax2.view_init(elev=10, azim=60)
ax2.plot_surface(X, Y, z, cmap="jet")

plt.show()
