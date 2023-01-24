# 齐次波动问题  数值解法
# Utt - a^2Uxx = 0, 0 < x < l, t > 0
# U(0, t) = 0, U(l, t) = 0, t >= 0
# U(x, 0) = sin(pi * x / l), Ut(x, 0) = sin(2 * pi * x / l)

import numpy as np
import matplotlib.pyplot as plt

l = 6
h = 0.1
sum_time = 10
k = 0.1  # 时间步长

N = int(l / h)  # 空间步数
M = int(sum_time / k)  # 时间的步数

s = 1 * k ** 2 / (h ** 2)

U = np.zeros([N + 1, M + 1])

Space = np.linspace(0, l, N + 1)
Time = np.linspace(0, sum_time, M + 1)
X, T = np.meshgrid(Space, Time)


def phi(t):
    temp = 0
    return temp

def psi(t):
    temp = 0
    return temp


def f(x):
    temp = np.sin(np.pi * x / l)
    return temp


def g(x):
    temp = np.sin(2 * np.pi * x / l)
    return temp


# 边界条件
for j in np.arange(0, M + 1):
    U[0, j] = phi(j * k)
    U[N, j] = psi(j * k)

# 初始条件
for i in np.arange(0, N + 1):
    U[i, 0] = f(i * h)
    U[i, 1] = f(i * h) + k * g(i * h) + s / 2.0 * (f((i + 1) * h) - 2 * f(i * h) + f((i - 1) * h))
# 递推关系
for j in np.arange(1, M - 1):
    for i in np.arange(1, N):
        U[i, j + 1] = 2 * (1 - s) * U[i, j] + s * U[i + 1, j] + s * U[i - 1, j] - U[i, j - 1]

# 画法1
# plt.figure(figsize=(12, 5))
# for i in range(M + 1):
#
#     plt.clf()  # 清除窗口内容
#     plt.title("{:.2f}".format(i * k))
#     plt.ylabel('u(x,t)', fontsize=20)
#     plt.xlabel('x', fontsize=20)
#     plt.xlim(0, 6)
#     plt.ylim(-2, 2)
#     plt.plot(Space, U[:, i])
#     plt.pause(0.01)


# # 画法2
U = U.T
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("X")
ax.set_ylabel("T")
ax.set_zlabel("Z")
ax.plot_surface(X, T, U, cmap="jet")
plt.show()
