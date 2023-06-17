"""Persamaan linier"""

import numpy as np
import scipy.linalg as la
import sympy as sp
sp.init_printing()

# Definisikan fungsi
# Buat matriks yang berisi Baris i dari matriks A ditempatkan pada baris j
def get_row(A,i,j):
  n = A.shape[0]
  E = np.zeros((n,n))
  E[j,i] = 1
  return E @ A

# Kalikan skala s pada baris i dari matriks A
def scale_row(A,i,s):
  n = A.shape [0]
  E = np.eye(n)
  E[i,i] = s
  return E @ A

# Dari persamaan pada soal latihan di peroleh matriks dengan nilai seperti pada output
A = np.array([[1, 1, 1],[1, 2, 4],[1, 3, 9]])
b = np.array([[1],[-1],[1]])
print(A)
print(b)

# Membuat Matriks Augmented dengan menggabungkan nilai variabel dengan konstanta
B = np.hstack([A,b])
print(B)

# Proses ELIMINASI pada baris 2 dan 3
B = B - (1/1)*get_row(B,0,1)
B = B - (1/1)*get_row(B,0,2)
print(B)

# Proses ELIMINASI pada baris 3
B = B - (2/1)*get_row(B,1,2)
print(B)

#PROSES Penyederhanan pada baris 3
B = scale_row(B,2,1/2)
print(B)

#PROSES SUBTITUSI pada baris ke 2
B = B - 3*get_row(B,2,1)
print(B)

#PROSES Penyederhanan pada baris 2
B = scale_row(B,1,1/(1))
print(B)

#PROSES SUBTITUSI pada baris ke 1
B = B - (get_row(B,1,0) + get_row(B,2,0))
print(B)

# Hasil akhir dengan menggunakan Modul Scipy.linalg
x = la.solve(A,b)
print(x)

# Hasil akhir dengan menggunakan Modul Sympy.solve
A2 = sp.Matrix(A)
b2 = sp.Matrix(b)
x2 = A2.solve(b2)
print(x2)

"""PERSAMAAN LINIER (2)"""

# metode Jacobi
tol = 1.0E-10 # Toleransi
delta = 1000 # nilai awal (untuk menghitung galat)
xn = 0.0
yn = 0.0
zn = 0.0
n = 0

# Perulangan untuk iterasi
while delta > tol:
 n+=1

 # xn+1 = F(xn)
 xnp1 = (1/2.0)*(2.0 - yn - zn)
 ynp1 = -(1/4.0)*(1.0 - xn - (2*zn))
 znp1 = (1/9.0)*(1.0 - xn - (3*yn))
 delta = abs(xnp1 - xn) + abs(ynp1 - yn) + abs(znp1 - zn)

 # Simpan untuk iterasi berikutnya
 xn = xnp1
 yn = ynp1
 zn = znp1

 print(n, xn, yn, zn)

# metode Gauss-Seidel.
tol = 1.0E-1 # Toleransi
delta = 1000 # nilai awal (untuk menghitung galat)
xn = 0.0
yn = 0.0
zn = 0.0
n = 0

# Perulangan untuk iterasi
while delta > tol:
 n+=1

 # xn+1 = F(xn)
 xnp1 = (1/2.0)*(2.0 - yn - zn)
 ynp1 = -(1/4.0)*(1.0 - xnp1 - (2*zn))
 znp1 = (1/9.0)*(1.0 - xnp1 - (3*ynp1))
 delta = abs(xnp1 - xn) + abs(ynp1 - yn) + abs(znp1 - zn)

 # Simpan untuk iterasi berikutnya
 xn = xnp1
 yn = ynp1
 zn = znp1

print(n, xn, yn, zn)

"""PERSAMAAN LINIER (3)"""

import numpy as np
import scipy.linalg as la
import sympy as sp
sp.init_printing()

# Definisikan fungsi
# Buat matriks yang berisi Baris i dari matriks A ditempatkan pada baris j
def get_row(A,i,j):
  n = A.shape[0]
  E = np.zeros((n,n))
  E[j,i] = 1
  return E @ A

#Kalikan skala s pada baris i dari matriks A
def scale_row(A,i,s):
  n = A.shape [0]
  E = np.eye(n)
  E[i,i] = s
  return E @ A

# Dari persamaan pada soal latihan di peroleh matriks dengan nilai seperti pada output
A = np.array([[1, 1, 0, 4],[2, -1, 5, 0],[5, 2, 1, 2],[-3, 0, 2, 6]])
b = np.array([[1],[3],[2],[-1]])
print(A)
print(b)

#Membuat Matriks Augmented
B = np.hstack([A,b])
print(B)

#Proses ELIMINASI pada baris 2,3, dan 4
B = B - (2/1)*get_row(B,0,1)
B = B - (5/1)*get_row(B,0,2)
B = B - (-3/1)*get_row(B,0,3)
print(B)

#Proses ELIMINASI pada baris 3 dan 4
B = B - ((-3)/(-3))*get_row(B,1,2)
B = B - ((-3)/3)*get_row(B,1,3)
print(B)

#Proses ELIMINASI pada baris 4
B = B - (7/(-4))*get_row(B,2,3)
print(B)

#PROSES Penyederhanaan pada baris 4
B = scale_row(B,3, -2/15)
print(B)

#PROSES SUBTITUSI pada baris 3
B = B - (-10)*get_row(B,3,2)
print(B)

#PROSES Penyederhanaan pada baris 3
B = scale_row(B,2,1/(-4))
print(B)

#PROSES SUBTITUSI pada baris 2
B = B - ((5*get_row(B,2,1)) + ((-8)*get_row(B,3,1)))
print(B)

#PROSES Penyederhanaan pada baris 2
B = scale_row(B,1,1/(-3))
print(B)

#PROSES SUBTITUSI pada baris 1
B = B - ((get_row(B,1,0)) + (0*get_row(B,2,0))+(4*get_row(B,3,0)))
print(B)

# Hasil akhir dengan menggunakan Modul Scipy.linalg
x = la.solve(A,b)
print(x)

# Hasil akhir dengan menggunakan Modul Sympy.solve
A2 = sp.Matrix(A)
b2 = sp.Matrix(b)
x2 = A2.solve(b2)
print(x2)