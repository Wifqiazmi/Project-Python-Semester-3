"""PERSMAAN DIFERENSIAL PARSIAL"""

"""METODE DIFUSI"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#jumlah grid
N = 50

#Parameter
dx = 0.02
dt = dx*dx/4
alpha = dt/(dx*dx)

#titik tengah
x0 = N*dx/2

#membuat array zeros sebanyak (N+1) untuk grid
U0 = np.zeros([N+1])
U = np.zeros([N+1])
Unew = np.zeros([N+1])

#array nilai x
x = np.arange(N+1)*dx - x0

#syarat awal
U0[25] = 10

#Iterasi persamaan difusi 
#jumlah itersi
nt = 20

Ut = []
s = []

#Iterasi syarat awal dan batas
for i in range(0, N+1):
    U[i] = U0[i]

for n in range(1, nt):
    #waktu
    t = n*dt

    #compute update
    for i in range(1, N):
        Unew[i] = U[i] + alpha*(U[i+1] - 2*U[i] + U[i-1])

        #save for next iteration
    for i in range(0,N+1):
        U[i] = Unew[i]
        #save for plotting
    if n%5 == 0:
        Ut.append(list(U))
        s.append('t = ' + str(t))

#visualisasi hasil setelan n iterasi

#tambahkan dta awal U0
Ut.insert(0,U0)
s.insert(0, 't = 0')
s.insert(1, 't = 0.0005')

#plot
for k in range(len(Ut)):
    plt.plot(x,Ut[k])

Vnew = np.zeros([N+1])

plt.title('Simulasi Difusi Gas')
plt.xlabel('x')
plt.ylabel('U(x,t)')
plt.xlim([-0.2,0.2])
plt.legend(s)
plt.show()


"""METODE PDP LAPLACE"""

#Jumlah grid
N = 50

#Membuat array zeros sebanyak (N+1)x(n+1) untuk grid
v = np.zeros([N+1,N+1])
#Inisialisasi syarat batas
for j in range(0,N+1):
    v[0,j] = 100

#Keadaan awal array dengan imshow
plt.imshow(v.transpose(), 
interpolation='nearest')
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.show()

#Iterasi persamaan laplace
for n in range(1000):
    for i in range(1,N):
        for j in range(1,N):
            v[i,j] = (v[i-1,j] + v[i+1, j] + v[i,j-1] + v[i,j+1])/4

#Visualisasi array hasil dengan inshow
plt.imshow(v.transpose(), interpolation='nearest')
plt.axis('off')
plt.show()

#membuat posisi grid dengan meshgrid
x = y = np.arange(N+1)*0.02
X, Y = np.meshgrid(x, y, sparse=False, indexing='ij')

#Visualisasi dengan contourf
plt.figure(figsize=(8,6))
plt.contourf(X, Y, v, 10, cmap=cm.coolwarm)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.colorbar()
plt.show()

#Visualisasi dengan axes 
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
cf = ax.contourf(X, Y, v, 10, cmap=cm.inferno)
fig.colorbar(cf, ax=ax)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.show()

#mengikuti contoh https://matplotlib.org/3.1.0/gallery/mplot3d/surfac3d.html
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(projection='3d')

#plot the surface
surf = ax.plot_surface(X, Y, v, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""METODE PDP GELOMBANG"""

#Jumlah grid
N = 50
#Parameter
c = 1
dx = 0.02
dt = dx/(2*c)
alpha = (c*dt/dx)**2
x0 = N*dx/2
#Membuat array zeros sebanyak (N+1) untuk n grid
U0 = np.zeros([N+1])
U1 = np.zeros([N+1])
Un = np.zeros([N+1])
Unm1 = np.zeros([N+1])
Unp1 = np.zeros([N+1])
 
#array nilai z
x = np.arange(N+1)*dx-x0
#syarat awal
a = 1
b = 100
#fungsi gelombang pada waktu t = 0
U0 = np.exp(-b*(x-0)**2)
#fungsi gelombang pada waktu t = dt
U1 = np.exp(-b*(x-c*dt)**2)
plt.plot(x,U0)
plt.plot(x,U1)
plt.show()

#iterasi persamaan difusi
#Jumlah iterasi

nt = 40
Unm1 = np.copy(U0)
Un = np.copy(U1)
Ut = []
s = []

for n in range(2,nt+1):
    t = n*dt
    for i in range(1,N):
         Unp1[i] = 2*Un[i] - Unm1[i] + alpha*(Un[i+1] - 2*Un[i] + Un[i-1])
    
    #safe for next iteration
    Unm1 = np.copy(Un)
    Un = np.copy(Unp1)
     #save for plotting
    if n%10 == 0:
        Ut.append(list(Un))
        s.append('t = ' + str(t))

#Visualisasi hasil setelah n iterasi
#Tambahkan data awal U0
Ut.insert(0,U0)
s.insert(0, 't = 0')
#plot
for k in range(len(Ut)):
    plt.plot(x,Ut[k])

plt.title('Simulasi Gelombang Skalar')
plt.xlabel('x')
plt.ylabel('U(x,t)')
plt.legend(s)
plt.show()
            


