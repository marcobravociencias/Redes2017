#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
import pyaudio
import Constants

# class MyApiServer():
#    def __init__(self, my_port = None):
#       pass


class FunctionWrapper:

    def __init__(self):
        self.buffer = list()
        self.stream = None

    def sendMessage_wrapper(self, message):
        """ **************************************************
        Procedimiento que ofrece nuestro servidor, este método será llamado
        por el cliente con el que estamos hablando, debe de
        hacer lo necesario para mostrar el texto en nuestra pantalla.
        ************************************************** """
        self.buffer.append(message)

    def ping(self):
        """ **************************************************
        Método que nos indica si el servidor se encuentra en servicio.
        ************************************************** """
        return True

    def vaciaBuffer(self):
        """ **************************************************
        Método que nos deja vacío el buffer del servidor donde guarda
        los mensajes y lo regresa.
        ************************************************** """
        buffer = ''
        for m in self.buffer:
            buffer += m
            print buffer
            self.buffer = list()
        return buffer

    def recibeAudio(self, audio):
        """ **************************************************
        Método que recibe el audio del cliente con el que se conecta el chat.
        ************************************************** """
        CHUNK = Constants.CHUNK
        CHANNELS = Constants.CHANNELS
        RATE = Constants.RATE
        RECORD_SECONDS = Constants.RECORD_SECONDS
        DELAY_SIZE = Constants.DELAY_SIZE
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(Constants.CHANNELS)
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()
