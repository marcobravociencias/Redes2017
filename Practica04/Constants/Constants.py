#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Puerto donde se establece la comunicación
PORT = "5000"
# Tiempo de espera en segundos entre cada actualización de obtención de
# mensajes
SLEEP = 1
# Tamaño máximo de la cola de multiprocessing utilizada para manejar hilos
QUEUE_MAX_SIZE = 10000
# Parámetros para el buffering de audio
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
CHUNKS_BUFFER = 50
RECORD_SECONDS = 5
DELAY_SIZE = RECORD_SECONDS * RATE / (1000 * CHUNK)
