#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:Funciones auxiliares                      #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
import socket


def get_ip_address():
    """**************************************************
    Método auxiliar que hace uso de internet para
    conocer la ip con la que contamos como usuarios
    **************************************************"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return "%s" % (s.getsockname()[0])

import threading


class MyThread(threading.Thread):

    """**************************************************
    Clase auxiliar que implementa el método stop, para que el hilo se detenga
    externamente
    **************************************************"""

    def __init__(self, target):
        super(MyThread, self).__init__(target=target)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def is_stop(self):
        return self._stop.isSet()
