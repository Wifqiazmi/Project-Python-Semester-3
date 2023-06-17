"""Penggunaan Python untuk menghitung turunan secara numerik (1)"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = symbols('x')
fx = x**3-2*x**2-x

# Mencetak nilai f(x) saat x = 1
print('fx=', fx.subs(x,1))

x0 = .25
h = .05

# Menghitung nilai f(x) saat x = x0-2h, x0-h, x0, x0+h, dan x0+2h
fm2 = fx.subs(x, x0-2*h)
fm1 = fx.subs(x, x0-h)
f0 = fx.subs(x, x0)
f1 = fx.subs(x, x0+h)
f2 = fx.subs(x, x0+2*h)

# Menghitung turunan pertama f(x) secara eksak
dfx = diff(fx,x,1)
df = dfx.subs(x,x0)

# Menghitung turunan pertama f(x) secara numerik dengan metode tengah
gc = (f1-fm1)/(2*h)
ec = (gc-df)/df

# Menghitung turunan pertama f(x) secara numerik dengan metode maju
gf = (f1-f0)/h
ef = (gf-df/df)

# Menghitung turunan pertama f(x) secara numerik dengan metode mundur
gb = (f0-fm1)/h
eb = (gb-df)/df

# Menghitung turunan kedua f(x) secara eksak
d2fx = diff(fx,x,2)
d2f = d2fx.subs(x,x0)

# Menghitung turunan kedua f(x) secara numerik dengan metode tengah
pc = (f1-2*f0+fm1)/(h**2)
ec2 = (pc-d2f)/d2f

# Membuat plot
xd = np.linspace(0,10,100)
df = lambdify(x,dfx)
ff = lambdify(x,fx)
dfd = df(xd)

gc = (ff(xd+h)-ff(xd-h))/(2*h)
gf = (ff(xd+h)-ff(xd))/h
gb = (ff(xd)-ff(xd-h))/h

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(6,6))
ax1.plot(xd, gc, 'or',label='central')
ax1.plot(xd, gf, 'xg',label='forward')
ax1.plot(xd, gb, '+r',label='backward')
ax1.plot(xd, dfd, '-k',label='eksak')

# Menampilkan plot
ax1.set_ylabel('turunan pertama')
ax1.legend(loc='upper right')

ax2.plot(xd, gc-dfd, '-k',label='central')
ax2.plot(xd, gf-dfd, ':b',label='forward')
ax2.plot(xd, gb-dfd, '--r',label='backward')
ax2.set_ylabel('kesalahan')
ax1.set_xlabel('x')
ax2.legend(loc='upper right')
fig.tight_layout()
plt.show()

"""Penggunaan Python untuk menghitung turunan secara numerik (2)"""
x = symbols('x')

# Fungsi yang dikerjakan
fx = sin(x)

# Mencetak nilai f(x) saat x = 1
print('fx=', fx.subs(x,1))

# Posisi untuk menghitung turunan numerik
x0 = 1.0

# Interval/spasi antara titik data
h = 0.1

# Membuat 5 data [f(x_i)]
# fm1 = f_[-1] dst
fm2 = fx.subs(x, x0 - 2*h)
fm1 = fx.subs(x, x0 - h)
f0 = fx.subs(x, x0 )
f1 = fx.subs(x, x0 + h)
f2 = fx.subs(x, x0 + 2*h)

# Turunan pertama eksak
dfx = diff(fx,x,1)
df = dfx.subs(x, x0)

# Turunan pertama numerik metode tengah (central)
gc = (f1 - fm1)/(2*h)

# Kesalahan relatif
ec = (gc - df)/df

# Turunan pertama numerik metode maju (forward)
gf = (f1 - f0)/h

# Kesalahan relatif
ef = (gf - df)/df

# Turunan pertama numerik metode mundur (backward)
gb = (f0 - fm1)/h

# Kesalahan relatif
eb = (gb - df)/df

# Turunan kedua eksak
d2fx = diff(fx, x, 2)
d2f = d2fx.subs(x, x0)

# Turunan kedua metode tengah (central)
pc = (f1 - 2*f0 + fm1)/(h**2)

# Kesalahan relatif
ec2 = (pc - d2f)/d2f

# Membuat plot
xd = np.linspace(0,10,100)

# Mengubah persamaan sympy menjadi fungsi python dengan lambdify()
df = lambdify(x, dfx)
ff = lambdify(x, fx)
dfd = df(xd)

# Hitung turunan numerik
gc = (ff(xd + h) - ff(xd - h))/(2*h)
gf = (ff(xd + h) - ff(xd))/h
gb = (ff(xd) - ff(xd - h))/h

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(6,6))
ax1.plot(xd, gc, 'or', label='central')
ax1.plot(xd, gf, 'xg', label='forward')

ax1.plot(xd, gb, '+r', label='backward')
ax1.plot(xd, dfd, '-k', label='eksak')

# Menampilkan plot
ax1.set_ylabel('turunan pertama')
ax1.legend(loc='upper right')

ax2.plot(xd, gc-dfd, '-k', label='central')
ax2.plot(xd, gf-dfd, ':b', label='forward')
ax2.plot(xd, gb-dfd, '--r', label='backward')
ax2.set_ylabel('kesalahan')
ax1.set_xlabel('x')
ax2.legend(loc='upper right')
fig.tight_layout()
plt.show()


"""tugas latihan"""
# Mendefinisikan variabel x sebagai simbol
x = symbols('x')

# Fungsi yang akan dikerjakan
fx = (x**3/3) + cos(x**2)

# Substitusi x = 1 dan tampilkan hasilnya
print('fx = ',fx.subs(x,1))

# Persyaratan persamaan
x0 = 1.0
h = 0.1

# Membuat 5 variabel substitusi x dan tampilkan hasilnya
fm2 = fx.subs(x, x0-2*h) # Nilai f(x-2h)
fm1 = fx.subs(x, x0-h) # Nilai f(x-1h)
f0 = fx.subs(x, x0) # Nilai f(x)
f1 = fx.subs(x, x0+h) # Nilai f(x+1h)
f2 = fx.subs(x, x0+2*h) # Nilai f(x+2h)

# Turunan pertama eksak
print("\nTurunan pertama eksak")
dfx = diff(fx, x, 1) # Menghitung turunan pertama fx terhadap x
print(dfx) # Menampilkan hasilnya
df = dfx.subs(x, x0) # Substitusi x dengan x0 pada hasil turunan pertama fx
print(df) # Menampilkan hasilnya

# Turunan pertama numerik metode tengah
print("\nTurunan pertama numerik metode tengah")
gc = (f1-fm1)/(2*h) # Menghitung turunan pertama dengan metode tengah
print(gc) # Menampilkan hasilnya
ec = (gc-df)/df # Menghitung error dari hasil turunan pertama dengan metode tengah
print("Error : ", abs(ec), "%") # Menampilkan error dalam persen

# Turunan pertama numerik metode maju
print("\nTurunan pertama numerik metode maju")
gf = (f1-f0)/h # Menghitung turunan pertama dengan metode maju
print(gf) # Menampilkan hasilnya
ef = (gf - df) / df # Menghitung error dari hasil turunan pertama dengan metode maju
print("Error : ", abs(ef), "%") # Menampilkan error dalam persen

# Turunan pertama numerik metode mundur
print("\nTurunan pertama numerik metode mundur")
gb = (f0-fm1)/h # Menghitung turunan pertama dengan metode mundur
print(gb) # Menampilkan hasilnya
eb = (gb-df)/df # Menghitung error dari hasil turunan pertama

"""Turunan kedua eksak"""
print("\nTurunan kedua eksak")
d2fx = diff(fx,x,2) # Menghitung turunan kedua fx terhadap x
print(d2fx) # Menampilkan hasilnya
d2f = d2fx.subs(x,x0) # Substitusi x dengan x0 pada hasil turunan kedua fx
print(d2f) # Menampilkan hasilnya

"""Turunan kedua numerik metode tengah"""
print("\nTurunan kedua numerik metode tengah")
pc =(f1-2*f0+fm1)/(h** 2) # Menghitung turunan kedua dengan metode tengah
print(pc) # Menampilkan hasilnya
ec2 = (pc - d2f) / d2f # Menghitung error dari hasil turunan kedua dengan metode tengah
print("Error : ", abs(ec2), "%") # Menampilkan error dalam persen

"""Turunan kedua numerik metode maju"""
print("\nTurunan kedua numerik metode maju")
pf = (f2-2*f1+f0)/h** 2 # Menghitung turunan kedua dengan metode maju
print(pf) # Menampilkan hasilnya
ef2 = (pf - d2f) / d2f # Menghitung error dari hasil turunan kedua dengan metode maju
print("Error : ", abs(ef2), "%") # Menampilkan error dalam persen

"""Turunan kedua numerik metode mundur"""
print("\nTurunan kedua numerik metode mundur")
pb = (f0-2*fm1+fm2)/h** 2 # Menghitung turunan kedua dengan metode mundur
print(pb) # Menampilkan hasilnya
eb2 = (pb-d2f)/d2f # Menghitung error dari hasil turunan kedua dengan metode mundur
print("Error : ", abs(eb2), "%") # Menampilkan error dalam persen

"""Grafik Turunan Pertama"""
xd = np.linspace(0, 10, 100) # Membuat 100 titik data dari x = 0 hingga x = 10
df = lambdify(x, dfx) # Mengubah dfx menjadi fungsi Python
ff = lambdify(x, fx) # Mengubah fx menjadi fungsi Python
dfd = df(xd) # Menghitung nilai turunan pertama fx pada setiap titik xd
gc = (ff(xd+h)-ff(xd-h))/(2*h) # Menghitung nilai turunan pertama dengan metode tengah pada setiap titik xd
gf = (ff(xd+h)-ff(xd))/h # Menghitung nilai turunan pertama dengan metode maju
gb = (ff(xd)-ff(xd-h))/h
fig,(ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(6,6))
ax1.plot(xd, dfd, color='r', label='Turunan Pertama Eksak')
ax1.plot(xd, gc, color='g', label='Turunan Pertama Numerik Metode Tengah')
ax1.plot(xd, gf, color='b', label='Turunan Pertama Numerik Metode Maju')
ax1.plot(xd, gb, color='m', label='Turunan Pertama Numerik Metode Mundur')
ax1.set_xlabel('x')
ax1.set_ylabel('Turunan Pertama')
ax1.legend(loc='best')

"""Grafik Turunan Kedua"""
d2fd = df(xd) # Menghitung nilai turunan kedua fx pada setiap titik xd
pc = (ff(xd+h)-ff(xd)+ff(xd-h))/(h** 2) # Menghitung nilai turunan kedua dengan metode tengah pada setiap titik xd
pf = (ff(xd+h)-ff(xd+h)+ff(xd))/h** 2 # Menghitung nilai turunan kedua dengan metode maju pada setiap titik xd
pb = (ff(xd)-ff(xd-h)+ff(xd-2*h))/h** 2 # Menghitung nilai turunan kedua dengan metode mundur pada setiap titik xd
ax2.plot(xd, d2fd, color='r', label='Turunan Kedua Eksak')
ax2.plot(xd, pc, color='g', label='Turunan Kedua Numerik Metode Tengah')
ax2.plot(xd, pf, color='b', label='Turunan Kedua Numerik Metode Maju')
ax2.plot(xd, pb, color='m', label='Turunan Kedua Numerik Metode Mundur')
ax2.set_xlabel('x')
ax2.set_ylabel('Turunan Kedua')
ax2.legend(loc='best')
plt.show()

