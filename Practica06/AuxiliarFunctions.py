# -*- coding: utf-8 -*-
#


class Autentica:
    # Clase que guarda en una archivo de texto llamado input.txt los usuarios
    # y las contraseñas con cada cararter en equivalencia su codigo ASCII + 5
    # @param usr usuario de la sesion
    # @param pas contraseña del usuario

    def __init__(self, usr, pas):
        self.usr = usr
        self.pas = pas

    #
    # Metodo para codificar las contraseñas por cada caracter, se toma su valor ASCII
    #	y se le suma 5
    #	@param password contraseña a "cifrar"
    #

    def codifica(self, password):
        lista = list(password)
        asci = [ord(a) for a in lista]  # Obtenemos el ascii de la palabra
        asci = [num+5 for num in asci]  # Sumamos 5 a cada valos ASCII
        return ''.join(chr(i) for i in asci)

    #
    # Metodo que toma una linea y la separa en usuario y contraseña
    #	@param linea la linea del archivo leida
    #
    def tokens(self, linea):
        x = linea.split()
        contra = x.pop()
        x.pop()  # :
        x.pop()  # Password
        usuario = x.pop()
        lista = list()
        lista.append(contra)
        lista.append(usuario)
        return lista

    #
    # Metodo que verifica que el usuario y la contraseña esten en la lista
    #@return True si esta, False en otro caso
    #

    def login(self):
        f = open('input.txt', 'r')  # Ruta desde main por que lo usa desde ahi.
        line = f.readline()
        while line != '':
            lista = self.tokens(line)  # Contrasena Usuario
            if self.usr == lista.pop():
            	print 'usuario existe'
                if self.codifica(self.pas) == lista.pop():
                	print 'contraseña correcta'
                	return True
                else:
                	print 'contraseña incorrecta'
                	return False
            line = f.readline()
        f.seek(0)  # Regresamos Apuntador
        f.close()
        return False
    #
    # Metodo que busca un usuario y su contraseña en la lista, si esta no lo agrega
    # en caso de no coincidir con un usuario ya registrado los agrega
    # @return True si agrega al usuario, False en otro caso
    #

    def registra(self):
        f = open('input.txt', 'r')
        line = f.readline()
        while line != "":
            lista = self.tokens(line)  # contra Usuario
            if self.usr == lista.pop():  # Concidio con el Usuario
                return False
            line = f.readline()
        f.seek(0)
        f.close()
        self.agrega()
        return True

    #
    # Metodo que agrega un usuario y su contraseña al archivo input.txt
    #

    def agrega(self):
        f = open('input.txt', 'a')
        password = self.pas
        linea = '\nusername : '+self.usr+' password : '+self.codifica(password)
        f.write(linea)
