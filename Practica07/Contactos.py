#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *

chat_class = uic.loadUiType("Lista_contactos.ui")[0]


class Contactos(QtGui.QMainWindow, chat_class):

    """docstring for Contactos"""

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def regresa_ip(self):
        ip = str(self.ip.text())  # cacha la ip con
        self.ip.clear()
        return ip
