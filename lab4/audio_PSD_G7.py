#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Lo de arriba es para que los IDE conozcan en que esta escrito este codigo 
###########################################################
# Puedes encontrar este codigo como objeto_ej4.py en:    ##
# https://sites.google.com/saber.uis.edu.co/comdig/sw    ##
###########################################################
###           IMPORTACION DE LIBRERIAS                  ###
###########################################################
# Libreria obligatoria
import numpy as np
from gnuradio import gr
 
# Librerias particulares
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes
from gnuradio import audio 
# Librerias para poder incluir graficas tipo QT
from gnuradio import qtgui
from PyQt5 import Qt # si no se acepta PyQt4 cambie PyQt4 por PyQt5
import sys, sip
 
# Ahora debes importar tu libreria. A continuacion suponemos que tu libreria ha sido
# guardada en un archivo llamado lib_comdig_code.py
import Lib_G7 as bloques 
 
 
###########################################################
###           LA CLASE DEL FLUJOGRAMA                   ###
###########################################################
class flujograma(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
 
        ################################################
        ###   EL FLUJOGRAMA                          ###
        ################################################
 
        # Las variables usadas en el flujograma
        samp_rate = 32000
        N= 1024
        # Los bloques usados
        audio_out=audio.sink(samp_rate,"")#uso salidas de audio
        audio_in=audio.source(samp_rate,"")#uso entradas de audio
        strtovec=blocks.stream_to_vector(gr.sizeof_float*1, N)
        e_fft=bloques.e_vector_fft_ff(N)
        average=bloques.vector_average_hob(N ,30)
        vsnk = qtgui.vector_sink_f(
            N,
            -samp_rate/2.,
            samp_rate/N,
            "Frecuency",
            "Magnitude",
            "Magnitude of FFT",
            2 # Number of inputs
        )
        vsnk.enable_autoscale(True)
        # conectando los bloques
        self.connect(audio_in,strtovec,e_fft,(vsnk,0))
        self.connect(e_fft, average, (vsnk,1))
        self.connect(audio_in,audio_out)
        
        

        # Graficando con QTGUI
        pyobj = sip.wrapinstance(vsnk.pyqwidget(), Qt.QWidget)
        pyobj.show()
 
###########################################################
###                LA CLASE PRINCIPAL                   ###
###########################################################
def main():
    # Def de aplicacion como QT GUI
    qapp = Qt.QApplication(sys.argv)
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    qapp.exec_()
 
# como el main lo hemos puesto como una funcion, ahora hay que llamarla
# podriamos escibir simplemete main(), pero es mas profesional asi:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass