#! /usr/bin/env python
# -*- coding: utf-8 -*-

PORT = "5000" # Puerto donde se establece la comunicación
SLEEP = 1 # Tiempo de espera en segundos entre cada actualización de obtención de mensajes
QUEUE_MAX_SIZE = 10000 # Tamaño máximo de la cola de multiprocessing utilizada para manejar hilos
# Parámetros para el buffering de audio
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
CHUNKS_BUFFER = 50