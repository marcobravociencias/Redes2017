import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import *
#from ../Code/ScientificCalculator import scientific
#from ../Code/archiva import archiva
sys.path.insert(0, '../Code/')
from ScientificCalculator import scientific
from archiva import archiva
from UsuarioNuevoGUI import Nuevo

noRegis = uic.loadUiType("noRegis.ui")[0]

class Error(QtGui.QMainWindow, noRegis):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

main_class = uic.loadUiType("calculadora.ui")[0]
class VentanaCalculadora(QMainWindow,main_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.boton_0.clicked.connect(self.cero)
        self.boton_1.clicked.connect(self.uno)
        self.boton_2.clicked.connect(self.dos)
        self.boton_3.clicked.connect(self.tres)
        self.boton_4.clicked.connect(self.cuatro)
        self.boton_5.clicked.connect(self.cinco)
        self.boton_6.clicked.connect(self.seis)
        self.boton_7.clicked.connect(self.siete)
        self.boton_8.clicked.connect(self.ocho)
        self.boton_9.clicked.connect(self.nueve)
        self.boton_divide.clicked.connect(self.divide)
        self.boton_igual.clicked.connect(self.igual)
        self.boton_producto.clicked.connect(self.producto)
        #
        self.boton_potencia.clicked.connect(self.potencia)
        self.boton_modulo.clicked.connect(self.modulo)
        #
        self.boton_punto.clicked.connect(self.punto)
        self.boton_resta.clicked.connect(self.resta)
        self.boton_suma.clicked.connect(self.suma)
        self.boton_borrar.clicked.connect(self.borra)

        self.usserNuevoDespliega.clicked.connect(self.agregaUsr)
        #self.calcuDisplay.setModified(False)
        
        
        self.w = None
        
    def agregaUsr(self):
        self.w = Nuevo()
        self.w.show()
        self.hide()
                
    
    def divide(self):
        self.agrega('/')
        self.opr='/'   
    
    def igual(self):
        opr = str(self.calcuDisplay.text()).replace(' ','')
        cal = scientific()
        y = 'Error'
        if '+' in opr:
            x =  opr.split('+')
            y = cal.suma(x.pop(), x.pop())

        if '-' in opr:
            x = opr.split('-')
            x.reverse()
            y = cal.resta(x.pop(), x.pop())

        if '*' in opr:
            x = opr.split('*')
            y = cal.multi(x.pop(), x.pop()) 

        if '/' in opr:
            x = opr.split('/')
            x.reverse()
            y = cal.div(x.pop(), x.pop())

        if '%' in opr: 
        	x = opr.split('%')
        	x.reverse()
        	y = cal.mod(x.pop(), x.pop())
        
        if '^' in opr: 
        	x = opr.split('^')
        	x.reverse()
        	y = cal.pot(x.pop(), x.pop())
        
        if not 'Error' in str(y):
            self.calcuDisplay.setText(str(y))
        else:
            print 'Error'
            self.calcuDisplay.setText(str(y))           

    def potencia(self):
        self.agrega('^')
        self.opr='^'

    def modulo(self):
        self.agrega('%')
        self.opr='%'
 
    def producto(self):
        self.agrega('*')
        self.opr='*'   
    
    def punto(self):
        self.agrega('.')

    def suma(self):
        self.agrega('+')
        self.opr='+'   

    def resta(self):
        self.agrega('-')
        self.opr='-'   

 
    def cero(self):
        self.agrega('0')

    def uno(self):
        self.agrega('1')
    
    def dos(self):
        self.agrega('2')

    def tres(self):
        self.agrega('3')

    def cuatro(self):
        self.agrega('4')

    def cinco(self):
        self.agrega('5')

    def seis(self):
        self.agrega('6')
    
    def siete(self):
        self.agrega('7')

    def ocho(self):
        self.agrega('8')

    def nueve(self):
        self.agrega('9')

    
    def agrega(self,cadena):
        opr = str(self.calcuDisplay.text())
        opr = opr+cadena
        self.calcuDisplay.setText(opr)

    def borra(self):
    	self.calcuDisplay.setText("")

#####

class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = Ventana()
        self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
        self.main.show()

    def byebye(self):
        self.exit(0)    
 
def main(args):
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)