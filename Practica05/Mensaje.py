#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time

class Mensaje(object):
    """Clase que define el formato para un mensaje"""
    def __init__(self, autor, texto, ip_origen):
        super(Mensaje, self).__init__()
        self.fecha = time.strftime("%H:%M:%S")
        self.autor = autor
        self.texto = texto
        self.leido = False
        self.ip_origen = ip_origen

    def setLeido(self,leido):
    	self.leido = leido
        
    def getLeido(self):
    	return self.leido