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
import sys, getopt
sys.path.insert(0, './Channel')
sys.path.insert(0, './GUI')
#sys.path.insert(0, './Constants')
from Login import *
from ApiServer import *
from ApiClient import * 

# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main(args):
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
   main(sys.argv)
