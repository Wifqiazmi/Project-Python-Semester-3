"""Persamaan Non Linier (1)"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt

# Definisi Fungsi f(x) dengan
def f(x):
  t = x*x -x -1
  return t

# Definisi Fungsi g(x) dengan
def g(x):
  t = sqrt(x+1) #1/(x-1)
  return t

# Penyelesaian menggunakan iterasi metode titik tetap pada fungsi g(x) = √(x - 1)
tol = 1.0E-1 # Toleransi (Epsilon)
delta = 1000 # Nilai awal (untuk menghitung galat)
xn = 0.0
xd = []

# Perulangan untuk iterasi
while delta > tol :
 # xn+1 = g (xn)
 xnp1 = g(xn)
 delta = abs(xnp1 - xn)

  #Simpan untuk iterasi berikutnya
 xn = xnp1
 xd.append(xn)
print(xd)

# Visualisasi<
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()

# Definisi Fungsi g(x) dengan
def g(x):
  t = 1/(x-1)
  return t
  
  # Penyelesaian menggunakan iterasi metode titik tetap pada fungsi g(x) = 1/(x-1)
tol = 1.0E-1 # Toleransi (epsilon)
delta = 1000 # nilai awal (untuk menghitung galat)
xn = 0.0
xd = []

# Perulangan untuk iterasi
while delta > tol :
 # xn+1 = g (xn)
 xnp1 = g(xn)
 delta = abs(xnp1 - xn)
 #Simpan untuk iterasi berikutnya
 xn = xnp1
 xd.append(xn)
print(xd)

# Visualisasi
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()

# Penyelesaian menggunakan iterasi metode biseksi
tol = 1.0E-1 # Toleransi (epsilon)
delta = 1000 # nilai awal (untuk menghitung galat)
a = 0.0
b = 1.0
fa = f(a)
fb = f(b)
xd = []
xn = b
# Perulangan untuk iterasi
while delta > tol:
   # Nilai tengah
   c = (a + b)/2.0
   fc = f(c)
   # Cek jika interval mengandung solusi
   if (fa*fc) < 0:
    b = c
    fb = fc
   else:
    a = c
    fa = fc

   xd.append(f(c))
   xnp1 = c
   delta = abs(xnp1 - xn)

   # Simpan untuk iterasi berikutnya
   xn = xnp1

print(xd)

# Visualisasi
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()

"""Persamaan Non Linier (2)"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

"""METODE Newton-Rapshon"""

# Definisi Fungsi f(x) dengan
def f(x):
  return x - np.exp(-2*(x*x))

# Definisi Turunan Fungsi f(x) dengan
def df(x):
  return 1 - ((-4*(x))*np.exp(-2*(x*x)))

# Penyelesaian menggunakan iterasi Newton-Raphson
tol = 1.0E-1 # Toleransi (epsilon)
delta = 1000 # nilai awal (untuk menghitung galat)
xn = 1.0
xd = []

# Perulangan untuk iterasi
while delta > tol :
 xnp1 = xn - f(xn)/df(xn)
 delta = abs(xnp1 - xn)
#Simpan untuk iterasi berikutnya
 xn = xnp1
 xd.append(xn)
 print(xd)

# Visualisasi
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()

"""Persamaan Non Linierr (2)"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# Definisi Fungsi f(x) dengan
def f(x):
  t = 1 - ((x*x)/2) + ((x*x*x*x)/24)
  return t

# Definisi Fungsi g(x) dengan
def g(x):
  t = ((x*x*x)/6)-x
  return t

# Penyelesaian menggunakan iterasi sekan
tol = 1.0E-1 # Toleransi (epsilon)
delta = 1000 # nilai awal (untuk menghitung galat)
xnm1 = 0.9 # x n-1
xn = 1.0 # x n
fnm1 = f(xnm1)
fn = f(xn)
xd = [xn]

# Perulangan untuk iterasi
while delta > tol :
  xnp1 = xn - fn*(xn - xnm1)/(fn - fnm1)
  delta = abs(xnp1 - xn)
  fnp1 = f(xnp1)

  #Simpan untuk iterasi berikutnya
  xnm1 = xn
  xn = xnp1
  fnm1 = fn
  fn = fnp1
  xd.append(xn)

  print (xd)

# Visualisasi
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()

# Penyelesaian menggunakan iterasi Regula Falsi
tol = 1.0E-1 # Toleransi (epsilon)
delta = 1000 # Nilai awal (untuk menghitung galat)
a = 0.9
b = 1.0
fa = f(a)
fb = f(b)
xd = []
xn = b
#Perulangan untuk iterasi
while delta > tol :
  c = b - fb*(b-a)/(fb - fa)
  fc = f(c)

  # Cek jika interval mengandung solusi
  if (fa*fc) < 0:
    b = c
    fb = fc
  else:
    a = c
    fa = fc 
    
  xd.append(c)
  xnp1 = c
  delta = abs(xnp1 - xn)

  #Simpan untuk iterasi berikutnya
  xn = xnp1

print(xd)

# Visualisasi
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()