import wave
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
llama = uic.loadUiType("./GUI/LlamaCursoGUI.ui")[0]


class LlamadaCurso(QMainWindow, llama):

    """ **************************************************
    Clase que inicia la ventana del chat.
    ************************************************** """

    def __init__(self, espera_mensaje_local, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
