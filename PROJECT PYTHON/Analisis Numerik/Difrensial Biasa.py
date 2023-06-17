"""PERSMAAN DIFERENSIAL BIASA"""
import numpy as np
import matplotlib.pyplot as plt
 
print()
print("|| OUTPUT EULER HASIL ITERASI 10 ||")
print()
 
#Nilai awal
x0 = 0
y0 = 1
dx = 0.02
 
#definisi fungsi dx/dy = -x*y
def f(x,y):
  return -x*y
 
x = dx*np.arange(11) + x0
y = np.zeros(11)
y[0] = y0
 
#Eksak dari -x*y yaitu exp(-x**2/2)
yeksak = np.exp(-x**2/2)
 
#iterasi Euler
for n in range (0,10):
  #tulis rumus Euler
  y[n+1] = y[n] + dx*f(x[n], y[n])
  #Cetak hasil
  print("step : ", x[n+1], "Euler : ", y[n+1], "Eksaknya : ", yeksak[n])
 
#Buat grafik
plt.plot(x,y, 'or')
plt.plot(x,yeksak, '-b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(["Metode Euler", "Eksak"])
plt.show()
print()


print()
print("|| OUTPUT EULER HASIL ITERASI 100 ||")
print()
#Nilai awal
x0 = 0
y0 = 1
dx = 0.2

#definisi fungsi dx/dy = -x*y
def f(x,y):
  return -x*y

x = dx*np.arange(101) + x0
y = np.zeros(101)
y[0] = y0

#Eksak dari -x*y yaitu exp(-x**2/2)
yeksak = np.exp(-x**2/2)

#iterasi Euler
for n in range (0,100):
  #tulis rumus Euler
  y[n+1] = y[n] + dx*f(x[n], y[n])
  #Cetak hasil
  print("step : ", x[n+1], "Euler : ", y[n+1], "Eksaknya : ", yeksak[n])

#Buat grafik
plt.plot(x,y, 'or')
plt.plot(x,yeksak, '-b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(["Metode Euler", "Eksak"])
plt.show()
print()

"""METOODE ITERASI HEUN"""

print()
print("|| OUTPUT METOODE ITERASI HEUN 10 ||")
print()

import numpy as np
import matplotlib.pyplot as plt
#Nilai awal
x0 = 0
y0 = 1
dx = 0.02

#definisi fungsi dx/dy = -x*y
def f(x,y):
  return -x*y

x = dx*np.arange(11) + x0
y = np.zeros(11)
y[0] = y0

yeksak = np.exp(-x**2/2)
#iterasi Heun
for n in range (0,10):
    z = y[n] + dx*f(x[n], y[n])
    y[n+1] = y[n] + 0.5*dx*(f(x[n], y[n]) +
   f(x[n+1], z))

    #Cetak hasil
    print("step : ", x[n+1], "Euler : ", y[n+1], "Eksaknya : ", yeksak[n])

#Buat grafik
plt.plot(x,y, 'or')
plt.plot(x,yeksak, '-b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(["Metode Heun", "Eksak"])
plt.show()
print()

"""METOODE ITERASI HEUN"""

print()
print("|| OUTPUT METOODE ITERASI HEUN 100 ||")
print()

import numpy as np
import matplotlib.pyplot as plt
#Nilai awal
x0 = 0
y0 = 1
dx = 0.2

#definisi fungsi dx/dy = -x*y
def f(x,y):
  return -x*y

x = dx*np.arange(101) + x0
y = np.zeros(101)
y[0] = y0

yeksak = np.exp(-x**2/2)
#iterasi Heun
for n in range (0,100):
    z = y[n] + dx*f(x[n], y[n])
    y[n+1] = y[n] + 0.5*dx*(f(x[n], y[n]) +
   f(x[n+1], z))

    #Cetak hasil
    print("step : ", x[n+1], "Euler : ", y[n+1], "Eksaknya : ", yeksak[n])

#Buat grafik
plt.plot(x,y, 'or')
plt.plot(x,yeksak, '-b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(["Metode Heun", "Eksak"])
plt.show()
print()

"""METODE RUNGE KUTTA ORDE KE-4"""

print()
print("|| OUTPUT METODE RUNGE KUTTA ITERASI 10 ||")
print()

import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 1
dx = 0.02

def z(x,y):
  return -x*y

x=dx*np.arange(11)+x0
y=np.zeros(11)
y[0] = y0
h = dx

yeksak = np.exp(-x**2/2)

#iterasi Runge-kutta orde 4
for k in range(0,10):
  rk1 = z(x[k], y[k])
  rk2 = z(x[k]+h/2, y[k]+h*rk1/2)
  rk3 = z(x[k]+h/2, y[k]+h*rk2/2)
  rk4 = z(x[k]+h, y[k]+h*rk3)
  y[k+1] = y[k]+(h/6)*(rk1+2*rk2+2*rk3+rk4)
  print("step : ", x[k+1], "Euler : ", y[k+1], "Eksaknya : ", yeksak[k])
  

#Buat grafik
plt.plot(x,y, 'or')
plt.plot(x,yeksak, '-b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(["Metode Runge-Kutta", "Eksak"])
plt.show()
print()

"""METODE RUNGE KUTTA ORDE KE-4"""

print()
print("|| OUTPUT METODE RUNGE KUTTA ITERASI 100 ||")
print()

import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 1
dx = 0.2

def z(x,y):
  return -x*y

x=dx*np.arange(101)+x0
y=np.zeros(101)
y[0] = y0
h = dx

yeksak = np.exp(-x**2/2)

#iterasi Runge-kutta orde 4
for k in range(0,100):
  rk1 = z(x[k], y[k])
  rk2 = z(x[k]+h/2, y[k]+h*rk1/2)
  rk3 = z(x[k]+h/2, y[k]+h*rk2/2)
  rk4 = z(x[k]+h, y[k]+h*rk3)
  y[k+1] = y[k]+(h/6)*(rk1+2*rk2+2*rk3+rk4)
  print("step : ", x[k+1], "Euler : ", y[k+1], "Eksaknya : ", yeksak[k])
  

#Buat grafik
plt.plot(x,y, 'or')
plt.plot(x,yeksak, '-b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(["Metode Runge-Kutta", "Eksak"])
plt.show()
print()

