import numpy as np
import matplotlib.pyplot as plt

h = 0.1 #空间步长
N = 10 #空间步数
k = 0.01 #时间步长
M = 100 #时间的步数
s = 1 / 4 * k/(h**2) #lambda*tau/h^2
U = np.zeros([N+1,M+1]) #建立二维空数组
Space = np.arange(0,(N+1)*h,h) #建立空间等差数列，从0到1，公差是h

#边界条件
for k in np.arange(0,M+1):
    U[0,k] = 0.0
    U[N,k] = 0.0

#初始条件
for i in np.arange(0,N + 1):
    U[i,0]= 100
print(U.shape)
# print(np.arange(0, N + 1))
#递推关系
for k in np.arange(0,M):
    for i in np.arange(1,N):
        U[i,k+1]=s*U[i+1,k]+(1-2*s)*U[i,k]+s*U[i-1,k]

#不同时刻的温度随空间坐标的变化
plt.plot(Space,U[:,1], 'b-', label='t=0',linewidth=1.0)
plt.plot(Space,U[:,20], 'g-', label='t=2/10',linewidth=1.0)
plt.plot(Space,U[:,30], 'b-', label='t=3/10',linewidth=1.0)
plt.plot(Space,U[:,60], 'k-', label='t=6/10',linewidth=1.0)
plt.plot(Space,U[:,90], 'r-', label='t=9/10',linewidth=1.0)
plt.plot(Space,U[:,100], 'y-', label='t=1',linewidth=1.0)
plt.ylabel('u(x,t)', fontsize=20)
plt.xlabel('x', fontsize=20)
# plt.xlim(0,1)
# plt.ylim(0,120)
plt.legend(loc='upper right')
plt.show()

#温度等高线随时空坐标的变化，温度越高，颜色越偏红
extent = [0,1,0,5]#时间和空间的取值范围
levels = np.arange(0,101.1,0.1)#温度等高线的变化范围0-10，变化间隔为0.1
plt.contourf(U,levels, origin='lower', extent = extent,cmap="jet")
plt.colorbar()
plt.ylabel('x', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.show()