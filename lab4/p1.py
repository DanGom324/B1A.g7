import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import math
N=200
k=2
f0=3000
n=np.linspace(0,N-1,N)

T = 1./f0
Tsamp=T/N
fsamp = 1./Tsamp
fmin = -fsamp/2
fmax = fsamp/2
fres = fsamp/N
f = np.linspace(fmin,fmax-fres,N) 
signal=np.cos(2.*math.pi*k*n/N)
#signal=np.exp(1.j*2.*math.pi*k*n/N)
fourier=np.fft.fft(signal)
fshift=np.fft.fftshift(fourier)
#a=(abs(fourier_mejor))**2
plot(f,fshift)
show()