#! /usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
# PURPOSE:Interfaz grafica de un cliente en PyQt4    #
#                                                    #
# Vilchis Dominguez Miguel Alonso                    #
#       <mvilchis@ciencias.unam.mx>                  #
#                                                    #
# Notes: El alumno tiene que implementar la parte    #
#       comentada como TODO(Instalar python-qt)      #
#                                                    #
# Copyright   16-08-2015                             #
#                                                    #
# Distributed under terms of the MIT license.        #
#################################################### #
import sys
import getopt
sys.path.insert(0, './Channel')
sys.path.insert(0, './GUI')
#sys.path.insert(0, './Constants')
from Login import *
from ApiServer import *
from ApiClient import *


def main(args):
    # **************************************************
    #  Definicion de la funcion principal
    #**************************************************
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)
