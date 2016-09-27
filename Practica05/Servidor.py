#!/usr/bin/env python
#-*- coding: utf-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Mensaje import *
import sys
import pyaudio
import Constants


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class ServidorChat:

    """
    Clase que define el servidor de un chat el cual recibe texto y audio
    """

    def __init__(self):
        self.mensajes = list()
        self.stream = None

    def ping(self):
        """
        Metodo que sirve para saber si el servidor esta activo
        """
        return True

    def recibe_mensaje(self, mensaje):
        """
        Metodo que agrega a una lista el mensaje que le pasan
        """
        print "servidor recibe mensaje: "+str(mensaje)
        self.mensajes.append(mensaje)

    def sin_leer(self):
        """
        Metodo que enlista los mensajes que aun no han sido leidos, los agrega a una lista para luego 
        ponerlos como leidos 
        """
        no_leidos = list()
        for m in self.mensajes:
            leido = m['leido']
            if not leido:
                no_leidos.append(m)
                m['leido'] = True
        return no_leidos

    def recibe_audio(self, audio):
        """
        Crea un objeto de tipo pyaudio con los parametros establecidos y reproduce en un stream que crea localmente con el
        parametro audio que recibe
        """
        CHUNK = Constants.CHUNK
        WIDTH = Constants.WIDTH
        CHANNELS = Constants.CHANNELS
        RATE = Constants.RATE
        DELAY_SECONDS = Constants.RECORD_SECONDS
        DELAY_SIZE = Constants.DELAY_SIZE
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(WIDTH)
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()
