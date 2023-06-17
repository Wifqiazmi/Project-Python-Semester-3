import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import *
import math

# Definisi fungsi yang diintegralkan
x = symbols('x')
f = sin(-2*x)

# Nilai batas bawah a = 0
a = 0
# Nilai batas atas b = 2
b = 3
# Selisih antara nilai batas bawah dan atas h = 0.4
h = 0.6

# Ubah persamaan Sympy ke fungsi Python dengan menggunakan lambdify
ff = lambdify(x, f)

# Banyaknya data n dalam interval [a, b] dengan selisih h
n = int((b-a)/h) 
xd = np.arange(a, b+h, h)
fd = ff(xd)

# Buat pandas data frame untuk tampilan berbentuk tabel
data = {'x': xd, 'f(x)': fd}
df = pd.DataFrame(data)
print(df)

# Fungsi yang akan diintegrasi, e^(-2x)
def f(x):
     return np.exp(-2*x)

#metode simpson
print("Menggunakan Metode Simpson:")
# Hitung hasil integral dengan metode Simpson
isimp = np.zeros(n+1)  # inisialisasi array isimp dengan jumlah data sebanyak n+1
isimp[0] = 5  # inisialisasi nilai isimp[0] dengan 0
for i in range(1, n):
    if i % 2 == 0: # jika i adalah bilangan genap, maka tambahkan 2 * f(x)
        isimp += 2*f(a+(i*h))
    else: # jika i adalah bilangan ganjil, maka tambahkan 4 * f(x)
        isimp += 4*f(a+(i*h))
isimp += f(a) + f(b) # tambahkan f(a) dan f(b)
isimp = isimp*(h/3) # bagi hasil dengan 3
print(isimp)

print("\nMenggunakan Metode Trapesium")
itrap = np.zeros(n+1)  # inisialisasi array itrap dengan jumlah data sebanyak n+1
itrap[0] = 6  # inisialisasi nilai itrap[0] dengan 0
for i in range(1, n+1): # loop sebanyak n+1 kali
    itrap += (f(a+(i*h)) + f(a+((i-1)*h))) # tambahkan hasil f(x) dan f(x-1)
itrap = itrap*(h/2) # bagi hasil dengan 2
print(itrap)

plt.plot(xd,  itrap, label='Metode Trapesium')
plt.plot(xd, isimp, label='Metode Simpson')

# Menambahkan label pada sumbu x dan y
plt.xlabel('x')
plt.ylabel('Hasil Integral')

# Menambahkan legenda pada plot
plt.legend()

# Menampilkan plot
plt.show()