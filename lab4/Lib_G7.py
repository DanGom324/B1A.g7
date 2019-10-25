from gnuradio import gr
import numpy as np
import math
####################################################
##     Plantilla: clase e_add_cc                  ##
####################################################
 
 
# Se recomienda que el nombre de la clase finalice con una o dos letras especiales:
# nombre_ff: cuando en el bloque sus entradas y salidas son senales reales y de tipo flotante
# nombre_f: el bloque solo tiene una entrada o una salida y es una senal real de tipo flotante
# En vez de "f" pueden usarse: c (senal compleja),  i (entera), b (binaria), etc.
# Nota: esta plantilla tambien puede ser consultada en la libreria comdig_Lib_Bloques, dentro del bloque b_help
 
# Un bloque puede ser de varios tipos y eso se define en la clase como:
# gr.sync_block: cuando es de tipo sincrono
# gr.top_block: cuando es el flujograma principal
 
# gr.decim_block: cuando hay k muestras en la entrada por cada muestra saliente
# gr.interp_block: cuando hay k muestras en la salida por cada muestra entrante
# gr.hier_block2: cuando el bloque es como un flujograma
# gr.basic_block: otros casos
class e_add_cc(gr.sync_block):  
 
    # Dentro de la funcion __init__(), deben definirse los parametros de configuracion del bloque.
    # A cada parametro se le da un valor por defecto
    # ejemplo 1, solo hay un parametro de configuracion: def __init__(self, amp=1.0)
    # ejemplo 2, hay dos parametros: def __init__(self, amp=1.0, samp_rate= 32000)
    # a continuacion esta el caso de un solo parametro que hemos llamado escala
    def __init__(self, escala=0.5):
 
        # En la siguiente funcion debes recordar que usaras:
        # sync: cuando tu bloque sea un bloque de tipo sincrono (por cada muestra entrante habra una saliente)
        # decim: cuando es un bloque decimador (por cada muestra saliente hay un numero entero de muestras entrantes)
        # interp: cuando es un bloque interpolador (por cada muestra entrante hay un numero entero de muestras salientes)
        # basic: cuando no hay relacion entre el numero de muestras entrantes y las salientes
        # mas en: https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_Python#3.3.1._Choosing_a_Block_Type
        gr.sync_block.__init__(
            self,
 
            # Lo siguiente es para definir el nombre que tendra nuestro bloque para los usuarios de GRC
            name='Plantilla_para_crear_bloques_cc', 
 
            # A continuacion se definen los tipos de senales de entrada y salida. Veamos algunos ejemplos:
            # [np.complex64]: cuando se tiene una sola senal y es compleja
            # [np.float32]: cuando se tiene una sola senal y es de tipo real y flotante
            # [np.float32, np.complex64]: cuando hay dos senales: una de tipo real flotante y la otra es compleja
            # otros casos: int8 o byte (entero de 8 bits, que en C++ se conoce como char)
            # No hemos explorado mas casos, pero no es tan sencillo. Uno supondria que otros casos posibles son:
            # int16 (en C++ se conoce como short), int32, int64. Los dos primeros funcionan, pero int64 no.
            # En el siguiente ejemplo hay dos entradas complejas y una salida real.
            in_sig=[np.complex64,np.complex64], 
            out_sig=[np.complex64]
        )
 
        # las variables que entran como parametros del bloque deben ser declaradas nuevamente asi:
        self.escala=escala
 
        # abajo se puede escribir lo que se le antoje al programador, por ejemplo:
        # self.coef=1.0: define la variable global coef y le asigna el valor 1.0
        # self significa que es una variable global, que se puede invocar directamente desde otras funciones.
        # En todo caso, para las cosas que se definan aqui hay que tener en cuenta que:
        # -  esto es parte del constructor de la clase, por lo tanto, por cada bloque que se cree con esta clase
        #    estas cosas se invocaran solo una vez
        # -  Se supone que lo que se cree aqui es para ser usado, de manera que deberia ser usado en work()
        # A continuacion vamos a suponer que necesitamos usar constante  coef=1.0
        self.coef = 1.0
 
    # La funcion work() siempre debe estar presente en un bloque. Es alli donde estara la logica del bloque 
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala/self.coef
        return len(out0)
 
####################################################
##     clase e_add_ff                             ##
####################################################
class e_add_ff(gr.sync_block):  
    """consiste en un bloque para una suma escalada de dos senales reales. Por lo tanto hay dos senales de entrada y una de salida. Si escala=0.5 lo que se logra es promediar las dos senales"""
     
    def __init__(self, escala=0.5):
 
        gr.sync_block.__init__(
            self,
            name='e_add_ff', 
            in_sig=[np.float32,np.float32], 
            out_sig=[np.float32]
        )
        self.escala=escala
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala

        return len(out0)


class e_vector_fft_ff(gr.sync_block):
    """este bloque calcula la fft en magnitud de una senal vectorial con N muestras 
    y devuelve N muestras de su espectro. NOTA: N deber ser una potencia de 2 (N=n**2)"""
 
    def __init__(self, N=128):  
        gr.sync_block.__init__(
            self,
            name='e_vector_fft_ff',   
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        self.N = N
 
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        out0[:]=np.square(abs(np.fft.fftshift(np.fft.fft(in0,self.N),1))) #magnitud al cuadrado
        return len(output_items[0])


class vector_average_hob(gr.sync_block):
    """ El bloque vector_averager_hob recibe trmas de tamano N de una senal, a medida que clacula una trama del mismo tamano N que va siendo la media de las tramas que va recibiendo. 
        Los parametros usados son:
        N:        Es el tamano del vector o trama
        Nensayos: Es el umbral que limita el numero maximo de promedios correctamente realizados. Cuando a la funcion se le ha invocado un numero de veces mayor a Nensayos, el promedio continua realizandose, pero considerando que el numero de promedios realizado hasta el momento ya no se incrementa, sino que es igual a Nensayos. 
    """

    def __init__(self, N, Nensayos):
        gr.sync_block.__init__(self, name="vector_average_hob", in_sig=[(np.float32, N)], out_sig=[(np.float32, N)])

        # Nuestras variables especificas
        self.N=N
        self.Nensayos=np.uint64=Nensayos
        self.med=np.empty(N,dtype=np.float64)
        self.count=np.uint64=0

    def work(self, input_items, output_items):

        # Traduccion de matrices 3D a 2D 
        in0 = input_items[0]
        out0=output_items[0]
        
        # El tamano de la matriz in0 es L[0]xL[1]=L[0]xN
        L=in0.shape

        # conteo de funciones muestras (filas de matriz) procesadas
        if self.count < self.Nensayos:
            self.count += L[0] 

        # La media de las funciones muestras (filas de matriz) que tiene in0
        mean=in0.mean(0)    

        # ajuste de la media ya calculada, con la media de in0
        self.med = (self.med*(self.count-L[0])+mean*L[0])/self.count

        # Entrega de resultado
        out0[:]=self.med
        return len(out0)