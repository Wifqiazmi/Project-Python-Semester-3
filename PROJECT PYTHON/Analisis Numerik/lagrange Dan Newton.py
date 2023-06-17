"""MENGGUNAKAN METODE LAGRANGE"""

from sympy import *
x = symbols('x')
t = symbols('t')
p = symbols('p')
# menggunakan Data x dan y
xd = [0, 2, 3]
yd = [1, 5, 0]
n = len (xd)
p = 0
 
# Menghitung polinom p_n(x)
for k in range(n):
 t = yd[k]
 
 # untuk menghitung L-k(x)
 for j in range (n):
   if k != j:
     t *= (x-xd[j])/(xd[k]-xd[j])
 p += t
 
# nilai Hasil akhir
p1 = expand(p)
p1

"""MENGGUNAKAN METODE NEWTON"""

from sympy import *
import numpy as np
x = symbols('x')
p = symbols('p')
 
from sympy import *
import numpy as np
x = symbols('x')
p = symbols('p')
# Data x dan y
xd = [0, 2, 3]
yd = [1, 5, 0]
n = len (xd)
p = 0
 
# Membuat tabel beda dibagi Newton
dd = np.zeros((n,n))
 
# Mengisi tabel dd[k,0]
for k in range(n):
 dd[k,0] = yd[k]
 
# Mengisi tabel dd[k,j]
for j in range(1,n):
 for k in range(j,n):
   dd[k,j] = ( dd[k,j-1] - dd[k-1,j-1] ) / (xd[k] - xd[k-j])
 
   # Menghitung polinom p_n(x)
   p = dd[n-1,n-1]
   for k in range(1,n):
     p = p * (x - xd[n-k-1]) + dd[n-k-1,n-k-1]
 
     # Hasil akhir
p2 = expand(p)
p2

"""MENGGUNAKAN METODE LAGRANGE"""

from sympy import *
x = symbols('x')
t = symbols('t')
p = symbols('p')
 
# Data x dan y
xd = [0, 1, 2, 3]
yd = [5, 3, 1, 2]
 
n = len (xd)
 
p = 0
 
# Menghitung polinom p_n(x)
for k in range(n):
  t = yd[k]
  # HItung L-k(x)
  for j in range (n):
    if k != j:
      t *= (x-xd[j])/(xd[k]-xd[j])
 
  p += t
 
# Hasil akhir
p1 = expand(p)
p1

"""MENGGUNAKAN METODE NEWTON

"""

from sympy import *
import numpy as np
x = symbols('x')
p = symbols('p')
 
# Data x dan y
xd = [0, 1, 2, 3]
yd = [5, 3, 1, 2]
n = len (xd)
p = 0
 
# Membuat tabel beda dibagi Newton
dd = np.zeros((n,n))
 
# Mengisi tabel dd[k,0]
for k in range(n):
 dd[k,0] = yd[k]
 
# Mengisi tabel dd[k,j]
for j in range(1,n):
  for k in range(j,n):
    dd[k,j] = ( dd[k,j-1] - dd[k-1,j-1] ) / (xd[k] - xd[k-j])
 
    # Menghitung polinom p_n(x)
    p = dd[n-1,n-1]
    for k in range(1,n):
      p = p * (x - xd[n-k-1]) + dd[n-k-1,n-k-1]
 
# Hasil akhir
p2 = expand(p)
p2

"""MENGGUNAKAN METODE LAGRANGE"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
 
# Data x dan y
xd = [6.0, 7.0, 7.5, 7.7, 7.8]
yd = [0.1506, 0.3001, 0.2663, 0.2346, 0.2514]
 
n = len (xd)
 
# Nilai x
x = 6.5
 
# HItung nilai interpolasi p_n(6.5)
p = 0
for k in range (n) :
  t = yd[k]
  # HItung L-k(x)
  for j in range (n):
     if k != j:
       t *= (x-xd[j])/(xd[k]-xd[j])
 
  p += t
# Hasil akhir
print(p)
 
# Posisi interpolasi sebanyak 101 titik
xi = xd[0] + np.arange(101)*(xd[n-1] - xd[0])/100
 
# Array untuk menampung yi
yi = np.zeros(101)
for i in range(101):
  x = xi[i]
  p = 0
  for k in range(n):
    t = yd[k]
 
    # HItung L-k(x)
    for j in range (n):
      if k != j:
        t *= (x-xd[j])/(xd[k]-xd[j])
    p += t
  yi[i] = p
 
# Visualisasi
plt.plot(xi,yi,'-b')
plt.plot(xd,yd,'or')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""MENGGUNAKAN METODE NEWTON"""

import numpy as np
# Menghitung nilai f(x) dari data
# f(x) p_n(x) interpolasi Newton
 
# Input data x[i] dan f[i]
xd = [6.0, 7.0, 7.5, 7.7, 7.8]
yd = [0.1506, 0.3001, 0.2663, 0.2346, 0.2514]
n = len(xd)
 
# input nilai x
x = 6.5
 
# Membuat tabel beda terbagi Newton
dd = np.zeros((n,n))
 
# Mengisi tabel dd[k,0]
for k in range(n):
 dd[k,0] = yd[k]
 
# Mengisi tabel dd[k,j]
for j in range(1,n):
  for k in range(j,n):
    dd[k,j] = ( dd[k,j-1] - dd[k-1,j-1] ) / (xd[k] - xd[k-j])
 
# Menghitung nilai polinom p_n(6.5)
p = dd[n-1,n-1];
for k in range(1,n):
  p = p * (x - xd[n-k-1]) + dd[n-k-1,n-k-1]
 
# Hasil akhir
print(p)
 
# Interpolasi pada sebanyak 101 titik
xi2 = xd[0] + np.arange(101)*(xd[n-1] - xd[0])/100
 
# Array untuk menampung nilai yi
yi2 = np.zeros(101)
for i in range(101):
  x = xi2[i]
  p = dd[n-1,n-1];
  for k in range (1,n):
    p = p * (x - xd[n-k-1]) + dd[n-k-1,n-k-1]
 
  yi2[i] = p
 
# Visualisasi
plt.plot(xi2,yi2,'-b')
plt.plot(xd,yd,'or')
plt.xlabel('x')
plt.ylabel('y')
plt.show()