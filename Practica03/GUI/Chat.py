#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *

main_class = uic.loadUiType("./GUI/ChatGUI.ui")[0]


class Chat(QMainWindow, main_class):

    """ **************************************************
    Clase que inicia la ventana del chat.
    ************************************************** """

    def __init__(self, espera_mensaje_local, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def getTexto(self):
        """ **************************************************
        Método que obtiene el texto de la casilla para escribir
        y lo regresa.
        ************************************************** """
        msj = str(self.text_send.toPlainText())
        self.text_send.clear()  # LImpiamos el texto
        return msj

    def setTexto(self, mensaje):
        """ **************************************************
        Método que pone el texto en la interfaz del chat.
        ************************************************** """
        self.text_receive.insertPlainText(mensaje)  # interfaz
