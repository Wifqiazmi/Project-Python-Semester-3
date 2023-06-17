"""WIFQI WIFAKUL AZMI
   21102277
   IF-09K"""

import numpy as np
import matplotlib.pyplot as plt
 
# Data x dan y
xd = [3.0, 3.4, 4.5, 5.7]
yd = [2.4771, 2.4829, 2.4843, 2.4871]
 
n = len (xd)
 
# Nilai x
x = 3.2
 
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