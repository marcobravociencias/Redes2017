#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import Constants
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
# sys.path.insert(0, '../Code/')
from AuxiliarFunctions import Autentica
import xmlrpclib


existe = uic.loadUiType("existe.ui")[0]


class Error(QtGui.QMainWindow, existe):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.botonRegresaLogin.clicked.connect(self.salir)

    def salir(self):
        self.hide()
exito = uic.loadUiType("exito.ui")[0]


class Exito(QtGui.QMainWindow, exito):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.botonRegresaLogin.clicked.connect(self.salir)

    def salir(self):
        self.hide()
main_class = uic.loadUiType("agregaUsuario.ui")[0]


class Nuevo(QMainWindow, main_class):

    def __init__(self, ip_contactos, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.agregaUsser.clicked.connect(self.agregaUsr)
        self.boton_salir.clicked.connect(self.salir)
        self.w = None
        self.o = None
        self.ip_contactos = ip_contactos
        self.servidor_contactos = xmlrpclib.ServerProxy("http://"+self.ip_contactos+":" + str(Constants.DIRECTORY_PORT), allow_none=True)

    def agregaUsr(self):
        usuario = str(self.usserNuevoText.text()).replace(' ', '')
        password = str(self.passNuevoText.text()).replace(' ', '')
        registra = self.servidor_contactos.agrega_usuario(usuario, password)
        if registra:
            self.w = Exito()
            self.w.show()
        else:
            self.o = Error()
            self.o.show()

    def salir(self):
        self.hide()
        exit(0)


class App(QApplication):

    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = Ventana()
        self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye)
        self.main.show()

    def byebye(self):
        self.exit(0)


def main(args):
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)
