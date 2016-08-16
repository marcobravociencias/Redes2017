# -*- coding: utf-8 -*-
from Calculator import calculator
#
#Clase que extiende la clase Calculator agregando mas operaciones
#
class scientific(calculator):
	#
	#Metodo que realiza la multiplicacion de 2 valores
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return multiplicacion de los valores, error en otro caso 
	#
	def multi(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)*float(num2)	
		else:
			return 'Error'
	#
	#Metodo que realiza la division de 2 valores
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return division de los valores, error en otro caso 
	#
	def div(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)/float(num2)			
		else:
			return 'Error'
	#
	#Metodo que realiza el mod de 2 valores, num1 mod num2
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return modulo de los valores, error en otro caso 
	#
	def mod(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)%float(num2)
		else:
			return 'Error'
	#
	#Metodo que realiza la potencia de 2 valores, num1**num2
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return potencia de los valores, error en otro caso 
	#
	def pot(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)**float(num2)
		else: 
			return 'Error'
#cal = scientific()
#c = cal.pot('2', '3')
#print c