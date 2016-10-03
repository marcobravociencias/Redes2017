#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import xmlrpclib
import time
import threading
import pyaudio
import numpy
import Constants
from Mensaje import *
from Chat import *
from InterfazLlamada import *
from ThreadParable import *
from Contactos import *
from functools import partial


class Cliente(object):

    """
    Clase que se encarga de comunicar la interfaz gráfica con las acciones entre
    los servidores
    """

    def __init__(self, nick, pwd, ip_local, ip_contactos):
        """
        nick: apodo del usuario de este cliente
        ip_local: dirección ip del equipo que ejecuta este cliente
        ip_remoto: dirección ip del equipo remoto con el que se comunica este chat
        """
        super(Cliente, self).__init__()

        # asignaciones a atributos a partir de los parámetros
        self.nick = nick
        self.pwd = pwd
        self.ip_local = ip_local
        self.ip_contactos = ip_contactos

        # inicializamos un proxy que se comunique con el servidor de contactos
        self.servidor_contactos = xmlrpclib.ServerProxy("http://"+self.ip_contactos+":" + str(Constants.DIRECTORY_PORT), allow_none=True)
        self.servidor_contactos.login([self.nick, self.ip_local, self.pwd])

        # Inicializamos la interfaz de lista de contactos
        self.contactos_ui()

        # iniciamos un hilo que monitorea los mensajes que han sido enviados al servidor local
        # y los dibuja en la interfaz gráfica correspondiente a cada conversación
        self.hilo_mensajes_recibidos = threading.Thread(target=self.espera_mensaje_remoto,  name='hilo_mensajes_recibidos')
        self.hilo_mensajes_recibidos.start()

        # lista de interfaces de chat, una por cada conversación
        self.lista_chats = list()

    def contactos_ui(self):
        """
        Configura una ventana con la lista de contactos
        """
        # Iniciamos una ventana de lista de conctactos
        self.contactos = Contactos()
        # da click en 'Actualiza' y se actualiza la lista de contactos conectados
        # self.contactos.actualiza.clicked.connect(self.actualiza_lista)
        # da click en 'Conectar' y se inicia un nuevo chat
        self.hilo_actualiza_lista = threading.Thread(target=self.actualiza_lista, name='hilo_actualiza_lista')
        self.hilo_actualiza_lista.start()
        self.contactos.inicia_chat.clicked.connect(self.inicia_chat)
        # da click en 'Desconectar' y se desconecta del chat
        self.contactos.desconecta.clicked.connect(self.desconectarse)
        self.contactos.show()

    def actualiza_lista(self):
        """
        Hace una petición al servidor de contactos para actualizar la lista de contactos
        disponibles
        """
        while True:
            time.sleep(5)
            self.contactos.lista.clear()
            listita = self.servidor_contactos.disponibles()
            self.contactos.lista.setRowCount(len(listita))
            self.contactos.lista.setColumnCount(2)
            header = (QStringList() << 'Usuario' << 'Dirección Ip')
            self.contactos.lista.setHorizontalHeaderLabels(header)
            i = 0
            for contacto in listita:
                self.contactos.lista.setItem(i, 0, QtGui.QTableWidgetItem(contacto[0]))
                self.contactos.lista.setItem(i, 1, QtGui.QTableWidgetItem(contacto[1]))
                i = i+1

    def inicia_chat(self):
        """
        Inicia un chat con la ip que indique en la campo de la interfaz
        """
        ip_remoto = self.contactos.regresa_ip()
        print "ip_remoto: " + str(ip_remoto)
        nuevo_chat = Chat(ip_remoto)
        # asociamos el botón mandar con la función lambda envia_mensaje y el parámetro
        # ip correspondiente para que dibuje los mensajes en la ventana de chat apropiada
        nuevo_chat.mandar.clicked.connect(partial(self.envia_mensaje, ip=ip_remoto))
        nuevo_chat.audio.clicked.connect(self.llamada)
        nuevo_chat.show()
        # agregamos la nueva interfaz a la lista de interfaces
        self.lista_chats.append(nuevo_chat)

    def inicia_chat_ip(self, ip_r):
        """
        Inicia un chat con la ip que indique el argumento
        """
        ip_remoto = ip_r
        print "ip_remoto ip: " + str(ip_remoto)
        nuevo_chat = Chat(ip_remoto)
        # asociamos el botón mandar con la función lambda envia_mensaje y el parámetro
        # ip correspondiente para que dibuje los mensajes en la ventana de chat apropiada
        nuevo_chat.mandar.clicked.connect(partial(self.envia_mensaje, ip=ip_remoto))
        nuevo_chat.audio.clicked.connect(self.llamada)
        nuevo_chat.show()
        # agregamos la nueva interfaz a la lista de interfaces
        self.lista_chats.append(nuevo_chat)

    def desconectarse(self):
        self.servidor_contactos.logout([self.nick, self.ip_local])
        # aqui despues de esto, destruye a todos los chats

    def espera_mensaje_remoto(self):
        """
        Verifica constantemente los mensajes que han llegado al servidor local
        y que no han sido leídos, después los dibuja en la interfaz gráfica
        """
        servidor_local = xmlrpclib.ServerProxy("http://"+self.ip_local+":" + str(Constants.CONTACT_PORT), allow_none=True)
        while True:
            # espera 1 segundo
            time.sleep(Constants.SLEEP_TIME)
            # le pide al servidor los mensajes nuevos
            sin_leer = servidor_local.sin_leer()
            # los dibuja en la interfaz gráfica
            self.dibuja_mensajes(sin_leer)

    def dibuja_mensajes(self, mensajes):
        """
        Recibe una lista de mensajes y los dibuja en la interfaz gráfica de chat correspondiente.
        Si no existe la ventana de chat crea una.
        """
        for m in mensajes:
            if not self.existe_chat(m['ip_origen']):
                self.inicia_chat_ip(ip_r=m['ip_origen'])
            for chat in self.lista_chats:
                if chat.ip_remoto == m['ip_origen']:
                    chat.ponTexto(m['fecha'], m['autor'], m['texto'])

    def existe_chat(self, ip):
        """
        Regresa True syss hay una interfaz de chat asociada a la ip que le pasan
        """
        for chat in self.lista_chats:
            if chat.ip_remoto == ip:
                return True
        return False

    def envia_mensaje(self, ip):
        """
        Envía un mensaje a la ip que le pasan
        """
        # buscamos la ventana de chat desde donde se enviará el mensaje
        for chat in self.lista_chats:
            if chat.ip_remoto == ip:
                # construye el mensaje a partir del texto que hay en el chat correspondiente
                mensaje = Mensaje(self.nick, chat.texto_actual(), self.ip_local)
                # envía el mensaje al servidor remoto
                servidor_remoto = xmlrpclib.ServerProxy("http://"+ip+":" + str(Constants.CONTACT_PORT), allow_none=True)
                servidor_remoto.recibe_mensaje(mensaje)
                # dibuja el mensaje en la ventana de chat correspondiente
                chat.ponTexto(mensaje.fecha, mensaje.autor, mensaje.texto)

    def llamada(self):
        """
        Empieza dos hilos cuyo trabajo es realizar el stream de audio desde esta máquina
        hasta el servidor remoto
        """
        return False  # aún no implementada
        import multiprocessing as mp

        # crea algo de tipo Interfaz Llamada para que eventualmente
        # el usuario vea que hay llamada en curso
        self.interfaz_llamada = InterfazLlamada()
        self.interfaz_llamada.termina.clicked.connect(self.termina_llamada)

        # muestra la ventanita de llamada en curso
        self.interfaz_llamada.show()

        # utilizamos una cola para almacenar datos de audio
        self.cola = mp.Queue(Constants.QUEUE_SIZE)

        # hilo que captura el audio local y lo mete en la cola
        #self.hilo_escucha = threading.Thread(target=self.escucha,name='hilo_escucha')
        self.hilo_escucha = ThreadParable(targetp=self.escucha, namep='hilo_escucha')
        self.hilo_escucha.start()
        # hilo que saca lo que hay en la cola y lo envía al servidor remoto
        #self.hilo_transmite = threading.Thread(target=self.transmite,name='hilo_transmite')
        self.hilo_transmite = ThreadParable(targetp=self.transmite, namep='hilo_transmite')
        self.hilo_transmite.start()

    def escucha(self):
        """
        Permanece en escucha permanente del audio local y mete los datos en la cola
        """
        # parámetros del stream de entrada
        CHUNK = Constants.CHUNK
        WIDTH = Constants.WIDTH
        CHANNELS = Constants.CHANNELS
        RATE = Constants.RATE
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(WIDTH)

        # stream que captura el audio
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        while True:
            # checamos si el usuario aún no termina la llamada
            if self.hilo_escucha.detenido():
                return 1

            # tamaño del buffer que almacena datos de audio
            n = Constants.BUFFER_SIZE
            # arreglo para almacenar el buffer
            frame = []

            # agregamos n muestras de audio del stream al arreglo frame
            for i in range(0, n):
                frame.append(stream.read(CHUNK))

            # convertimos la "cadena" frame a datos binarios con el tipo de dato uint8
            datos_binarios = numpy.fromstring(''.join(frame), dtype=numpy.uint8)

            # verificamos que la cola no esté llena y si lo está sacamos algo
            if self.cola.full():
                self.cola.get_nowait()

            # metemos los datos binarios a la cola
            self.cola.put(datos_binarios)

    def transmite(self):
        """
        Permanentemente toma los datos (binarios) que hay en la cola y los envía
        al servidor remoto
        """
        while True:
            # checamos si el usuario aún no termina la llamada
            if self.hilo_transmite.detenido():
                return 1
            # primer elemento de la cola
            d = self.cola.get()
            # convertimos a una instancia de datos binarios
            data = xmlrpclib.Binary(d)
            # los enviamos al servidor remoto
            self.servidor_remoto.recibe_audio(data)

    def termina_llamada(self):
        """
        Termina los hilos correspondientes a la llamada de voz y cierra la ventanita
        """
        self.hilo_escucha.detener()
        self.hilo_transmite.detener()
        self.interfaz_llamada.close()
