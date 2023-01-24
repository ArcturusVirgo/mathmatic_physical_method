# -- coding: utf-8 --
# @Time: 2021/5/17 22:26
# @Author: Zavijah
# @File: demo_1.py
# @Software: PyCharm
# @Purpose:三维图像的形式
# 求解热传导方程
# $$
# \begin{cases}
# 	u_t-a^2u_{xx}=0\\
# 	u\left( 0,t \right) =u\left( l,t \right) =0\\
# 	u\left( x,0 \right) =\varphi \left( x \right)\\
# \end{cases}
# $$

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sym

a = 1
l = 10
x = np.linspace(0, 10, 100)
t = np.linspace(0, 5, 1000)
X, Y = np.meshgrid(x, t)


def u(x, t):
    def phi(z):  # phi函数
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


z = u(X, Y)
fig = plt.figure("3D Surface")
# 设置为3D图片类型
ax3d = Axes3D(fig)
ax3d.set_xlabel("X")
ax3d.set_ylabel("T")
ax3d.set_zlabel("U")
ax3d.plot_surface(X, Y, z, cmap="jet")
plt.show()
