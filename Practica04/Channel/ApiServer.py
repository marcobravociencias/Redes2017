#! /usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import sys
import pyaudio
import Constants
import cv2
import numpy
import threading
from cStringIO import StringIO
from numpy.lib import format

# class MyApiServer():
#    def __init__(self, my_port = None):
#       pass


class FunctionWrapper:

    def __init__(self):
        self.buffer = list()
        self.stream = []
        self.frames = []
        self.hiloReproduceVideo = threading.Thread(target=self.reproduceVideo)
        self.hiloReproduceVideo.setDaemon(True)
        # self.hiloReproduceVideo.start()
        self.hiloReproduceAudio = threading.Thread(target=self.reproduceAudio)
        self.hiloReproduceAudio.setDaemon(True)
        # self.hiloReproduceAudio.start()

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
        self.stream.append(audio.data)

    def toArray(self, s):
        f = StringIO(s)
        arr = format.read_array(f)
        return arr

    def recibeVideo(self, video):
        # print 's: recibo frame'
        self.frames.append(self.toArray(video.data))
        cv2.imshow('Servidor',self.frames.pop(0))
        # if len(self.frames) > 0:
        #     cv2.imshow('Servidor',self.frames.pop(0))
        # cv2.destroyAllWindows()

    def reproduceAudio(self):
        CHUNK = Constants.CHUNK
        CHANNELS = Constants.CHANNELS
        RATE = Constants.RATE
        RECORD_SECONDS = Constants.RECORD_SECONDS
        DELAY_SIZE = Constants.DELAY_SIZE
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(Constants.CHANNELS)
        while True:
            stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
            if len(self.stream) > 0:
                data = self.stream.pop(0)
                stream.write(data)
            stream.close()
        p.terminate()

    def reproduceVideo(self):
        while True:
            if len(self.frames) > 0:
                cv2.imshow('Servidor', self.frames.pop(0))
                # if cv2.waitKey(1) & 0xFF==ord('q'):
                #     break
        cv2.destroyAllWindows()
