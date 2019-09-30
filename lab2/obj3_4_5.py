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
    def __init__(self, x,y):#constructor de Calc_cient
        Calc_bas.__init__(self, x,y)#constructor de Calc_bas
        self.x = x
        self.y = y


    def media(self,x):
        z = (sum(x)/len(x))
        return(z)
    
    def mediac(self,x):
        x=x**2
        z = (self.media(x))
        return(z)
    def varianza(self,x):
        x = (x-self.media(x))**2
        z = (self.media(x))
        return(z)
    def desviacion(self,x):
        z = np.sqrt(self.varianza(x))
        return(z)




x = np.array(input('Introduzca el primer numero a operar: '))
#print(x)
y = np.array(input('Introduzca el segundo numero a operar: '))
#print(y)
m = input('seleccione la operacion a realizar: \n 1)Suma \n 2)Resta \n 3)Division \n 4)Multiplicacion \n 5)Media \n 6)Media Cuadratica \n 7)Varianza \n 8)Desviacion \n')

Calc1 = Calc_bas(x,y)
Calc_cient = Calc_cient(x,y)
if m==1:
    Z = Calc_cient.suma(x,y)
    print('Rta:',Z)
elif m==2: 
    Z = Calc_cient.resta(x,y)
    print('Rta:',Z)
elif m==3:
    Z = Calc_cient.division(x,y)
    print('Rta:',Z)
elif m==4:
    Z = Calc_cient.multiplicacion(x,y)
    print('Rta:',Z)
elif m==5:
    Z = Calc_cient.media(x)
    print('Rta:',Z)
elif m==6:
    Z = Calc_cient.mediac(x)
    print('Rta:',Z)
elif m==7:
    Z = Calc_cient.varianza(x)
    print('Rta:',Z)
elif m==8:
    Z = Calc_cient.desviacion(x)
    print('Rta:',Z)
else:
    pass
    print("Opcion no encontrada, intente de nuevo.")