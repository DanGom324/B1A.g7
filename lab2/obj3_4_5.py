import numpy as np 
#primer objetivo
#def suma(x,y):
#   z = x+y
#    return z


class Calc_bas:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def suma(self,x,y):
        z = x+y
        return z
    def resta(self,x,y):
        z = x-y
        return z
    def division(self,x,y):
        z = x/y
        return z
    def multiplicacion(self,x,y):
        z = x*y
        return z 

class Calc_cient(Calc_bas):




x = np.array(input('Introduzca el primer numero a operar: '))
#print(x)
y = np.array(input('Introduzca el segundo numero a operar: '))
#print(y)
m = input('seleccione la operacion a realizar: \n 1)suma \n 2)resta \n 3)division \n 4)multiplicacion \n')

Calc1 = Calc_bas(x,y)
if m==1:
    Z = Calc1.suma(x,y)
    print(Z)
elif m==2: 
    Z = Calc1.resta(x,y)
    print(Z)
elif m==3:
    Z = Calc1.division(x,y)
    print(Z)
else:
    Z = Calc1.multiplicacion(x,y)
    print(Z)