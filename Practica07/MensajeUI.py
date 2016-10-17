#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *

chat_class = uic.loadUiType("Mensaje.ui")[0]


class MensajeUI(QtGui.QMainWindow, chat_class):

    """docstring for Contactos"""

    def __init__(self, mensaje, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.mensaje.setText(mensaje)
        self.boton.clicked.connect(self.close)