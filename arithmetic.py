
class Calculator():
	"""Simple Calculator for two integers"""
	
	# Purpose: Add Two Integers
	# Contract: Integer, Integer -> Integer
	def add(self, first_int, second_int):
		return first_int + second_int
	
	# Purpose: Subtract Two Integers
	# Contract: Integer, Integer -> Integer
	def subtract(self, first_int, second_int):
		return first_int - second_int

	# Purpose: Multiply Two Integers
	# Contract: Integer, Integer -> Integer
	def multiply(self, first_int, second_int):
		return first_int * second_int

	# Purpose: Divide Two Integers and returns Quotient 
	# Contract: Integer, Integer -> Integer
	def divide(self, first_int, second_int):
		if second_int == 0:
			raise ZeroDivisionError

		return first_int / second_int

	# Purpose: Divide Two Integers and returns Remainder 
	# Contract: Integer, Integer -> Integer
	def modulo(self, first_int, second_int):
		if second_int == 0:
			raise ZeroDivisionError
		
		return first_int % second_int

	# Purpose: Perform arithmetic operation
	# Contract: Integer, Integer -> Integer
	def calculate(self, operator, first_int, second_int):
		if operator == '+':
			return self.add(first_int, second_int)
		elif operator == '-':
			return self.subtract(first_int, second_int)
		elif operator == '*':
			return self.multiply(first_int, second_int)
		elif operator == '/':
			return self.divide(first_int, second_int)
		elif operator == '%':
			return self.modulo(first_int, second_int)
		else:
			raise ValueError('Incorrect Operator')
		