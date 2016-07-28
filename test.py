from arithmetic import Calculator 
import unittest

class TestCalculator(unittest.TestCase):
	'''Unit Test Cases for Calculator Class'''

	#Sets up the environment before each test case
	def setUp(self):
		self.calculate = Calculator()

	# Test Cases for Add
	def testAdd(self):	
		self.assertEqual(5, self.calculate.calculate('+', 2, 3))
		self.assertEqual(3, self.calculate.calculate('+', 3, 0))
		self.assertEqual(2, self.calculate.calculate('+', 3, -1))

	# Test Cases for Subtract
	def testSubtract(self):
		self.assertEqual(-1, self.calculate.calculate('-', 2, 3))
		self.assertEqual(-3, self.calculate.calculate('-', 0, 3))
		self.assertEqual(4, self.calculate.calculate('-', 3, -1))
		
	# Test Cases for Multiply
	def testMultiply(self):
		self.assertEqual(6, self.calculate.calculate('*', 2, 3))
		self.assertEqual(0, self.calculate.calculate('*', 3, 0))
		self.assertEqual(-3, self.calculate.calculate('*', 3, -1))

	# Test Cases for Divide
	def testDivide(self):
		self.assertEqual(2, self.calculate.calculate('/', 8, 3))
		self.assertRaises(ZeroDivisionError,
							self.calculate.calculate, '/', 3, 0)
		self.assertEqual(-1, self.calculate.calculate('/', 3, -4))
		self.assertEqual(-2, self.calculate.calculate('/', 3, -2))

	# Test Cases for Modulo
	def testModulo(self):
		self.assertEqual(2, self.calculate.calculate('%', 8, 3))
		self.assertRaises(ZeroDivisionError,
							self.calculate.calculate, '%', 3, 0)
		self.assertEqual(-1, self.calculate.calculate('%', 3, -4))
		self.assertEqual(-3, self.calculate.calculate('%', 7, -5))

	# Test Cases for Wrong Operator
	def testWrongOp(self):
		self.assertRaises(ValueError, 
							self.calculate.calculate, 'as', 5, 9)

		

unittest.main()
