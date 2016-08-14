from Calculator import calculator
class scientific(calculator):
	
	def multi(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)*float(num2)	
		else:
			return 'Error'

	def div(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)/float(num2)			
		else:
			return 'Error'
	def mod(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)%float(num2)
		else:
			return 'Error'

	def pot(self, num1, num2):
		if self.verifica(num1, num2):
			return float(num1)**float(num2)
		else: 
			return 'Error'
#cal = scientific()
#c = cal.pot('2', '3')
#print c