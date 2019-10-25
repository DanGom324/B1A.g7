import numpy as np
import math
from matplotlib import pyplot as plt

fo = 1000.
k = 1
N = 50

n = np.linspace(0,N-1,N)
signal1 = np.cos(2.*math.pi*k*n/N)
signal2 = np.exp(1.j*2.*math.pi*k*n/N)
s_fft = np.fft.fftshift(np.fft.fft(signal2))
s_fftpow = abs(s_fft)**2
T = 1./fo
Ts = T/N
Fs = 1./Ts
Fmin = -Fs/2.
Fresol=Fs/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
plt.stem(f,s_fftpow)
plt.title('FFT '+str(N)+' Muestras, frecuencia '+str(int(fo))+' [Hz], k = '+str(k))
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.show()