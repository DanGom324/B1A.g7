import numpy as np


def media(x):
    z = (sum(x)/len(x))
    return(z)

#parametros de la senal
A1 = 20         
A2 = 10
A3 = 4
w1 = np.pi
w2 = np.pi/4
w3 = np.pi/3
# vector de tiempo que discretiza y acota la senal
t = np.linspace(0, 3.0, num=100, endpoint=False)
# ejemplo de senal a tratar
y = A1*np.sin(w1*t) + A2*np.sin(w2*t) + A3*np.sin(w3*t)

M = media(y)
print (y)
print(M)


