import numpy as np
import matplotlib.pyplot as plt

l = 5
a = 1 / 2

h = 0.1
k = 0.01

Max_t = 10

n = int(l / h)
m = int(Max_t / k)

U = np.zeros([n, m])

s = (a ** 2 * k) / (h ** 2)


def f_1(t):
    temp = 0
    return temp


def f_2(t):
    temp = 0
    return temp


def phi(x):
    temp = 100
    return temp


for i in range(n):
    U[i, 0] = phi(i * h)

for j in range(1, m):
    U[0, j] = f_1(j * k)
    U[n - 1, j] = f_2(j * k)

for j in range(m - 1):
    for i in range(1, n - 1):
        U[i, j + 1] = (1 - 2 * s) * U[i, j] +\
                      s * (U[i + 1, j] + U[i - 1, j])

x = np.linspace(0, l, n)
y = np.linspace(0, Max_t, m)
X, Y = np.meshgrid(x, y)
U = U.T
fig = plt.figure()
ax2 = fig.add_subplot(projection='3d')
ax2.set_xlabel("X")
ax2.set_ylabel("T")
ax2.set_zlabel("U")
ax2.plot_surface(X, Y, U, cmap="jet")
plt.show()
