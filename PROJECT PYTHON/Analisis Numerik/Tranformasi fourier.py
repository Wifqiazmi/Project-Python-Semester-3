from numpy import exp, pi
import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

"""WIFQI WIFAKUL AZMI"""
"""21102277"""

init_printing()

def f(x):
    return np.sin(x)+np.sin(2*x)

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

def fourier_coefficients(f, N):
    a0 = 0
    an = np.zeros(N+1)
    bn = np.zeros(N+1)
    L  = 4*np.pi
    for n in range(N+1):
        an[n] = (2/L) * np.trapz(f(x) * np.cos(n*x), x=x)
        bn[n] = (2/L) * np.trapz(f(x) * np.sin(n*x), x=x)
    return a0, an, bn

N = 10

a0, an, bn = fourier_coefficients(f, N)
f_fourier = a0 + np.sum([an[n]*np.cos(n*x)+bn[n]*np.sin(n*x)
                        for n in range(1, N+1)], axis=0)
fig = plt.subplots(figsize=(15, 10))
plt.plot (x, f(x), 'b', label='f(x)')
plt.plot (x, f_fourier, 'r', label='Fourier series')
plt.grid()
plt.legend()
plt.show()


#deret fourier sinus
def fourier_series(x, n_harmonics):
    series = np.zeros_like(x)
    for k in (1, n_harmonics+1):
        series += (1/k)*np.sin(k*x)
    return series

#buat data
x = np.linspace(0, 2*np.pi, 1600)
y = fourier_series(x, 10)

#Ttampilkan plot
plt.grid()
plt.plot(x, y)
plt.show()

h = 1000
P = 8

def fourier_series(x, n_harmonics):
    series = np.zeros_like(x)
    for k in range(1, n_harmonics + 1):
        series += (P*2 / (np.pi*k)) * np.sin(P * np.pi*k * x / h)
    return series

x = np.linspace(0, h, 1000)
y1 = fourier_series(x, 1)
y2 = fourier_series(x, 3)
y3 = fourier_series(x, 5)
y4 = fourier_series(x, 10)
y5 = fourier_series(x, 20)
y6 = fourier_series(x, 50)

square_wave = np.piecewise(x, [x < 5, x >= 5], [1, -1])

fig = plt.subplots(figsize=(15, 10))
plt.plot(x, y1, label='1 harmonik')
plt.plot(x, y2, label='3 harmonik')
plt.plot(x, y3, label='5 harmonik')
plt.plot(x, y4, label='10 harmonik')
plt.plot(x, y5, label='20 harmonik')
plt.plot(x, y6, label='50 harmonik')
plt.plot(x, square_wave, linestyle='dotted', label='Gelombang asli')
plt.legend()
plt.grid()
plt.show()


#t is the independent variable
T = np.pi #period value to the pi
P = 5. #banyaknya gelombang terhadap T
BT = -6. #initian value of t (begin time)
ET = 6. #final value of t (end time)
FS = 1060 #number of discrete values of t between BT and ET
#the periodic real-valued function f(t) with period egual to P

f = lambda t: (((t % T) - (T/ 2.)))**3

#all discrete values of t in the interval from BT and ET
t_range = np.linspace(BT, ET, FS)
y_true = f(t_range) #the true f(t)
#y_true
#function that computes the real fourier couples of coefficients (a0, 0), (al, b1)...(aN, bN)
def compute_real_fourier_coeffs(func, N):
    result = []
    for n in range(N+1):
        an = (P/T) * spi.quad(lambda t: func(t) * np.cos(P * np.pi * n* t/ T), 0, T)[0]
        bn = (P/T) * spi.quad(lambda t: func(t) * np.sin(P * np.pi * n* t/ T), 0, T)[0]
        result.append((an, bn))
        an
    return np.array(result)

#function that computes the real form Fourier series using an and bn coefficients
def fit_func_by_fourier_series_with_real_coeffs(t, AB):
    result = 0.
    A = AB[:,0]
    B = AB[:,1]
    for n in range(0, len(AB)):
        if n > 0:
            result += A[n] * np.cos(P * np.pi * n * t / T) + B[n] * np.sin(P * np.pi * n * t / T)
        else:
            result = A[0]/P
    return result

maxN = 10
COLs = 2 #cols of plt
ROWs = 1 + (maxN-1)  // COLs #rows of plt
plt.rcParams['font.size'] = 12
fig, axs = plt.subplots(ROWs, COLs, figsize=(25, 12.5)) #ukuran dari hasil grafik yg ditampilkan
fig.tight_layout(rect=(0, 0, 1, 0.95), pad=3.0)
fig.suptitle('f(t) = x^3 where P=' + str(P))

#plot, in the range from BT to ET, the true f(t) in blue and the approximation in red
for N in range(1, maxN + 1):
    AB = compute_real_fourier_coeffs(f, N)
    #AB contains the list of couples of (an, bn) coefficients for n in 1..N interval.
    y_approx = fit_func_by_fourier_series_with_real_coeffs(t_range, AB)
    #y approx contains the discrete values of approximation obtained by the Fourier series
    row = (N-1) // COLs
    col = (N-1) % COLs
    axs[row, col].set_title('case N=' + str(N))
    axs[row, col].scatter(t_range, y_true, color='blue', s=1, marker='.')
    axs[row, col].scatter(t_range, y_approx, color='red', s=2, marker='+')
    axs[row, col].legend(('$f(t) $', 'Deret Fourier'))
    plt.xlabel( '$t$')
    plt.ylabel( '$y$')
plt.show()

t = symbols('t')
n = symbols('n', integer=True, positive=True)
k = symbols('k', integer=True, positive=True)
f = Piecewise((1, t <= 1/2), (-1, t > 1/2))
T = 1
P = 2
f
plot(f, (t, 0, 1), nb_of_points=1000, ylim=(-1, 1), title='Sinyal Kotak')
a0 = integrate(f, (t, 0, T))
a0

fx = f*cos(n*P*pi*t)
fx

an = (P/T)*integrate(fx, (t, 0, T))
an

fx1 = f*sin(n*P*pi*t)
fx1

bn = (P/T) * integrate(fx1, (t, 0, T))
bn

m = 7
ff = a0/P+Sum(cos(k*P*pi*t) * an.subs(n, k), (k, 1, m)) + \
Sum(sin(k*P*pi*t)*bn.subs(n, k), (k, 1, m))
ff

ff2 = simplify(ff)
ff2

g = lambdify(t, f)
h = lambdify(t, ff2)
tt = np.arange(1000) * .01
gg = g(tt)
hh = h(tt)
# ukuran dari hasil grafik yg ditampilkan
fig = plt.subplots(figsize=(25, 12.5))
plt.plot(tt, gg)
plt.plot(tt, hh)
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.legend(['$f(t)$', 'Deret Fourier'])
plt.show()

"""TRANSFORMASI FOURIER"""
import matplotlib.cm as cm
from scipy.fft import ifftn
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq

"""WIFQI WIFAKUL AZMI"""
"""21102277"""

n = 100
dt = .1
ts = np.arange(n)*dt
f1 = .2
f2 = 1
ft = np.exp(2j*np.pi*f1*ts)+.2*np.exp(2j*np.pi*f2*ts)
plt.stem(ts, ft.real, use_line_collection=True)
plt.title('Bagian Riil')
plt.xlabel('$t$')
plt.ylabel('$f(t) $')
plt.show()

plt.stem(ts, ft.imag, use_line_collection=True)
plt.title('Bagian Imajiner')
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.show()

Fs = 1/dt
ff = fft(ft)
freq = fftfreq(100, .1)
plt.stem(freq, np.abs(ff), use_line_collection=True)
plt.xlabel('$f$')
plt.ylabel('$Abs [F(f)]$')
plt.show()

# sampling rate
sr = 100
# sampling interval
ts = 1.0/sr
t = np.arange(0, 1, ts)
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)
freq = 4
x += np.sin(2*np.pi*freq*t)
freq = 7
x += 0.5 * np.sin(2*np.pi*freq*t)
plt.figure(figsize=(8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')
plt.show()

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi*k * n / N)
    X = np.dot(e, x)
    return X

X = DFT(x)
# calculate the frequency
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T
plt.figure(figsize=(8, 6))
plt.stem(freq, abs(X), 'b', markerfmt=" ", basefmt="-b", use_line_collection=True)
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq) | ')
plt.show()

x = np.arange(-500, 501, 1)
wavelength = 200
y = np.sin(2 * np.pi*x / wavelength)
plt.plot(x, y)
plt.show()

X = np.arange(-500, 501, 1)
X, Y = np.meshgrid(x, x)
wavelength = 200
grating = np.sin(2 * np.pi * X / wavelength)
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()

# gratings.py
X = np.arange(-500, 501, 1)
X, Y = np.meshgrid(x, x)
wavelength = 200
angle = np.pi / 9
grating = np.sin(2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) /
wavelength)
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()

# gratings.py
x = np.arange(-500, 501, 1)
X, Y = np.meshgrid(x, x)
wavelength = 200
angle = 0
grating = np.sin(
2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) / wavelength)
plt.set_cmap("gray")
plt.subplot(121)
plt.imshow(grating)

# Calculate Fourier transform of grating
ft = np.fft.ifftshift(grating)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)
plt.subplot(122)
plt.imshow(abs(ft))
plt.xlim([480, 520])
plt.ylim([520, 480]) # Note, order is reversed for y
plt.show()

def FFT(x):
    N = len(x)
    if N == 1:
        return x
    else:
         X_even = FFT(x[::2])
         X_odd = FFT(x[1::2])
         factor = \
        np.exp(-2j*np.pi*np.arange(N) / N)
    X = np. concatenate(
        [X_even+factor[:int(N/2)]*X_odd,
        X_even+factor[int(N/2):]*X_odd])
    return x
# sampling rate
sr = 128
# sampling interval
ts = 1.0/sr
t = np.arange(0, 1, ts)
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)
freq = 4
x += np.sin(2*np.pi*freq*t)
freq = 7
x += 0.5 * np.sin(2*np.pi*freq*t)
plt.figure(figsize=(8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')
plt.show()

X = FFT(x)
# calculate the frequency
N = len(X)
n = np.arange(N)

T = N/sr
freq = n/T
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.stem(freq, abs(X), 'b', markerfmt=" ",basefmt="-b", use_line_collection=True)
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]
# normalize the amplitude
X_oneside = X[:n_oneside]/n_oneside
plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'b', markerfmt=" ",basefmt="-b", use_line_collection=True)
plt.xlabel('Freq (Hz)')
plt.ylabel('Normalized FFT Amplitude |X(freq)|')
plt.tight_layout()
plt.show()

def gen_sig(sr):
    ts = 1.0/sr
    t = np.arange(0, 1, ts)
    freq = 1.
    x = 3*np.sin(2*np.pi*freq*t)
    return x
# sampling rate =2048
sr = 2048
FFT(gen_sig(sr))
N = 30
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N, N))
xf[0, 5] = 1
xf[0, N-5] = 1
Z = ifftn(xf)
ax1.imshow(xf, cmap=cm.Reds)
ax4.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 0] = 1
xf[N-5, 0] = 1
Z = ifftn(xf)

ax2.imshow(xf, cmap=cm.Reds)
ax5.imshow(np. real(Z), cmap=cm.gray)

xf = np.zeros((N, N))
xf[5, 10] = 1
xf[N-5, N-10] = 1
Z = ifftn(xf)
ax3.imshow(xf, cmap=cm. Reds)
ax6.imshow(np. real(Z), cmap=cm.gray)
plt.show()
