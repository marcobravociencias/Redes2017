#! /usr/bin/env python
# -*- coding: utf-8 -*-
from ApiServer import MyApiServer
from ApiClient import MyApiClient


class RequestChannel():

    """
    Contiene los métodos necesarios para hacer uso de los métodos de un
    contacto (ApiClient)
    """

    def __init__(self, arg):
        self.arg = arg

class BidirectionalChannel():
	"""
	Canala de comunicación bidireccional (ApiServer + ApiClient)
	"""
	def __init__(self, arg):
		self.arg = arg
		