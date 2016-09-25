#! /usr/bin/env python
# -*- coding: utf-8 -*-
from ApiServer import MyApiServer
from ApiClient import MyApiClient


class RequestChannel():

    """
    Contiene los métodos necesarios para hacer uso de los métodos de un
    contacto (internamente ApiClient).
    Se crea una instancia cada vez que Bob quiere hablar con Alice.
    """

    def __init__(self, arg):
        self.arg = arg

class BidirectionalChannel():
	"""
	Canal de comunicación bidireccional (internamente ApiServer + ApiClient).
	"""
	def __init__(self, arg):
		self.arg = arg
		