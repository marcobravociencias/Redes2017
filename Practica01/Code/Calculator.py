#
#Clase calculadora que cuenta con las operaciones de Suma y Resta
#


class calculator:
	# -*- coding: utf-8 -*-
	#
	#Metodo que realiza la suma de 2 valores
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return suma de los valores, error en otro caso 
	#
	def suma(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)+float(num2)
		else:
			return 'Error'
	#
	#Metodo que realiza la resta de 2 valores
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return resta de los valores, error en otro caso 
	#
	def resta(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)-float(num2)
		else:
			return 'Error'

	#
	#Metodo que verifica que la cadena que se pasa a la interfaz sea
	# un numero
	# @param num1 primer operando
	# @param num2 segundo operando
	# @return True en caso de que sean numeros, False en otro caso 
	#
	def verifica(self, num1, num2):
		if num1.isdigit() and num2.isdigit():
			return True
		else:
			try:
				float(num1)
				float(num2)
				return True
			except ValueError:
				print 'Son letras : '+num1+' '+num2
				return False
#cal = calculator();
#c = cal.resta('2','3')
#print c 
