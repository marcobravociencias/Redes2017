import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
import threading
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
sys.path.insert(0, '../Channel')
from ApiServer import *
from ApiClient import *


class RequestHandler(SimpleXMLRPCRequestHandler):

    """ **************************************************
    Clase que inicializa la ventana para la conexcion del chat y todos
    los servicios.
    ************************************************** """
    rpc_paths = ('/RPC2',)

main_class = uic.loadUiType("./GUI/LoginGUI.ui")[0]


class Ventana(QMainWindow, main_class):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.boton_login.clicked.connect(self.OK)

    def OK(self):
        """ **************************************************
        Metodo que toma de la interfaz las ip's, y el nombre de usuario e inicializa
        los servidores y la instancia del usuario.
        ************************************************** """
        usuario = str(self.text_usser.toPlainText())
        ip1 = str(self.text_ip1.toPlainText())
        ip2 = str(self.text_ip2.toPlainText())
        self.hiloSer = threading.Thread(
            target=self.IniciaServidor, args=(ip1,))
        self.hiloSer.start()
        self.hide()
        self.client = MyApiClient(usuario, ip1, ip2)

    def IniciaServidor(self, ip1):
        """ **************************************************
        Metodo que inicializa el servidor al cual le llegan los mensajes.
        ************************************************** """
        server = SimpleXMLRPCServer(
            (ip1, 8000), requestHandler=RequestHandler, allow_none=True)
        server.register_introspection_functions()
        server.register_instance(FunctionWrapper())
        print "Listening on port 8000..."
        try:
            server.serve_forever()
            print 'Use Control-C to exit'
        except KeyboardInterrupt:
            print 'Exiting'


class App(QApplication):

    """ **************************************************
    Clase principal del chat.
    ************************************************** """

    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = Ventana(None)
        self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye)
        self.main.show()

    def byebye(self):
        self.exit(0)
