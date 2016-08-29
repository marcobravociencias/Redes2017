#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
import pyaudio

# class MyApiServer():
#    def __init__(self, my_port = None):
#       pass


class FunctionWrapper:

    def __init__(self):
        self.buffer = list()
        self.stream = None

    def sendMessage_wrapper(self, message):
        """ **************************************************
        Procedimiento que ofrece nuestro servidor, este metodo sera llamado
        por el cliente con el que estamos hablando, debe de
        hacer lo necesario para mostrar el texto en nuestra pantalla.
        ************************************************** """
        self.buffer.append(message)

    def ping(self):
        """ **************************************************
        Metodo que nos indica si el servidor se encuentra en servicio.
        ************************************************** """
        return True

    def vaciaBuffer(self):
        """ **************************************************
        Metodo que nos deja vacio el buffer del servidor donde guarda
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
        Metodo que recibe el audio del cliente con el que se conecta el chat.
        ************************************************** """
        CHUNK = 1024
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        DELAY_SIZE = RECORD_SECONDS * RATE / (1000 * CHUNK)
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        p.terminate()
