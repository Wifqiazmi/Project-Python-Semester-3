"""Penggunaan Python untuk menghitung integrasi secara numerik (1)"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import pandas as pd

x = symbols ('x')
#definisi fungsi yang di integralkan
f = x**3 - x
#batas integral
a = 0
b = 2
#ubah persamaan sympy ke fungsi python
ff = lambdify(x,f)

#buat data sebanyak n+1
#dari x = a...b
n = 10
xd = np.linspace(a,b,n+1)
fd = ff(xd)
dx = xd[1] - xd[0]

#buat pandas data frame untuk tampilan berbentuk tabel
data = {'x': xd, 'f(x)': fd}
df = pd.DataFrame(data)
df 

#metode eksak
ieksak = integrate(f,(x,a,b))
ieksak

#metode trapesium
s = 0
for i in range(1,n):
    s += fd[i]
itrap = (dx/2)*(fd[0] + 2*s + fd[n])
itrap

#galat relatif 
errtrap = (itrap - ieksak)/ieksak
errtrap

#metode simpson
s1 = 0
s2 = 0
for i in range (1,n,2):
    s1 += fd[i]
for i in range(2,n-1,2):
    s2 += fd[i]
isimp = (dx/3)*(fd[0] + 4*s1 + 2*s2 + fd[n])
isimp

errsimp = (isimp - ieksak)/ieksak
errsimp

#metode gauss legendre
y = symbols('y')
#subtitusi variabel x dengan (a+b)/2 + (b-a)y/2
g = f.subs(x, (a+b)/2 +(b-a)*y/2)
g

#ybahlah ke persamaan sympy ke fungsi python
gg = lambdify(y,g)

#menggunakan gauss-legendre 2 titik
w1 = 1.0
w2 = 1.0
x1 = -1/np.sqrt(3)
x2 = 1/np.sqrt(3)
ig12 = ((b-a)/2)*(w1*gg(x1) + w2*gg(x2))
ig12

errg12 = (ig12 - ieksak)/ieksak
errg12

#menggunakan gauss-legendre 3 titik
w1 = 5/9
w2 = 8/9
w3 = 5/9
x1 = -np.sqrt(3/5)
x2 = 0
x3 = np.sqrt(3/5)
ig13 = ((b-a)/2)*(w1*gg(x1) + w2*gg(x2) + w3*gg(x3))

errg13 = (ig13 - ieksak)/ieksak
errg13

"""Tugas latihan"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import *

# Definisi fungsi yang diintegralkan
x = symbols('x')
f = x + 2**2 - 2*x - 1

# Batas integral
a = 0
b = 3

# Ubah persamaan Sympy ke fungsi Python dengan menggunakan lambdify
ff = lambdify(x, f)

# Buat data sebanyak n + 1 dari x = a sampai b
n = 10
xd = np.linspace(a, b, n + 1)
fd = ff(xd)
dx = xd[1] - xd[0]

# Buat pandas data frame untuk tampilan berbentuk tabel
data = {'x': xd, 'f(x)': fd}
df = pd.DataFrame(data)
print(df)

# Metode Eksak
print("\nMetode Eksak")
ieksak = integrate(f, (x, a, b))
print(ieksak)

# Metode Trapesium
print("\nMetode Trapesium")
itrap = np.zeros(n+1)  # inisialisasi array itrap dengan jumlah data sebanyak n+1
itrap[0] = 0  # inisialisasi nilai itrap[0] dengan 0
itrap[n] = 0  # inisialisasi nilai itrap[n] dengan 0
for i in range(1, n):
    itrap[i] = (dx/2)*(fd[i-1] + fd[i])  # hitung nilai itrap[i] dengan menggunakan formula metode trapesium
print(itrap)

# Metode Simpson
print("\nMetode Simpson")
isimp = np.zeros(n+1)  # inisialisasi array isimp dengan jumlah data sebanyak n+1
isimp[0] = 0  # inisialisasi nilai isimp[0] dengan 0
isimp[n] = 0  # inisialisasi nilai isimp[n] dengan 0
for i in range(1, n):
    isimp[i] = (dx/3)*(fd[i-1] + 4*fd[i] + fd[i+1])  # hitung nilai isimp[i] dengan menggunakan formula metode Simpson
print(isimp)

# Metode Gauss-Legendre
print("\nMetode Gauss-Legendre")
y = symbols('y')
# Substitusi variabel x dengan (a+b)/2 + (b-a)y/2
g = f.subs(x, (a+b)/2 + (b-a)*y/2)
print(g)

# Ubah ke persamaan Sympy ke fungsi Python
gg = lambdify(y, g)

# Menggunakan Gauss-Legendre 2 titik
print("\nMetode Gauss-Legendre 2 titik")
w1 = 1.0
w2 = 1.0
x1 = -1/np.sqrt(3)
x2 = 1/np.sqrt(3)
igl2 = ((b-a)/2)*(w1*gg(x1) + w2*gg(x2))
print(igl2)

# Galat
# Galat
errg12 = (igl2 - ieksak)/ieksak
print("Galat : ", errg12)

# Menggunakan Gauss-Legendre 3 titik
print("\nMetode Gauss-Legendre 3 titik")
w1 = 5/9
w2 = 8/9
w3 = 5/9
x1 = -np.sqrt(3/5)
x2 = 0
x3 = np.sqrt(3/5)
igl3 = ((b-a)/2)*(w1*gg(x1) + w2*gg(x2) + w3*gg(x3))
print(igl3)

# Galat
errg13 = (igl3 - ieksak)/ieksak
print("Galat : ", errg13)

# Membuat plot dari hasil integral numerik yang diperoleh dari masing-masing metode
plt.plot(xd, itrap, label='Metode Trapesium')
plt.plot(xd, isimp, label='Metode Simpson')
plt.plot(x2, igl2, label='Metode Gauss-Legendre 2 titik')
plt.plot(x3, igl3, label='Metode Gauss-Legendre 3 titik')

# Menambahkan label pada sumbu x dan y
plt.xlabel('x')
plt.ylabel('Hasil Integral')

# Menambahkan legenda pada plot
plt.legend()

# Menampilkan plot
plt.show()



