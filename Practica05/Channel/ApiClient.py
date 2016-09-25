#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
sys.path.insert(0, '../Constants')
from Constants import CHAT_PORT
from AuxiliarFunctions import *

"""**************************************************
Clase que genera un proxy para poder hacer uso de
los procedimientos remotos que ofrece la api del contacto
**************************************************"""


class MyApiClient:

    def __init__(self, contact_ip=None, contact_port=None):
        if contact_port:
            contact_ip = get_ip_address()
            self.server = xmlrpclib.ServerProxy("http://" + contact_ip + ":" + contact_port, allow_none= True)
        elif contact_ip:
            self.server = xmlrpclib.ServerProxy("http://"+self.ip+":"+Constants.PORT, allow_none=True)
        else:
            raise ValueError('The values of fields are not consistent MyApiClient.__init__')
