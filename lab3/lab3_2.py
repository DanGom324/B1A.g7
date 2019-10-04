#!/usr/bin/env python
##################################################
# LO QUE HAY QUE IMPORTAR
################################################## 
from gnuradio import audio
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes
 
from PyQt5 import QtGui, QtCore, QtWidgets
import sys, sip

#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
###################################################### 

class mi_primer_esquema(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
 
        # Make a local QtApp so we can start it from our side
        self.qapp = QtWidgets.QApplication(sys.argv)
 
        samp_rate = 1e6
        fftsize = 2048
 
        self.src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 1, 1, 0)
        self.nse = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1)
        self.add = blocks.add_cc()
        self.thr = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)
 
        self.snk = qtgui.sink_c(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )
 
        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)
 
        # Tell the sink we want it displayed
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), QtWidgets.QWidget)
        self.pyobj.show()
 
def main():
    tb = mi_primer_esquema()
    tb.start()
    tb.qapp.exec_()
 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass