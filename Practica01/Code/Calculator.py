class calculator:

	def suma(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)+float(num2)
		else:
			return 'Error'

	def resta(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)-float(num2)
		else:
			return 'Error'

	
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
