#!/usr/bin/env python3

"""
A Simple working CRUD example to show Method Chain

Possible operations are: do_oprn, sum, subtract, multiple,
						 division, plus, addition, add,
						 minus, subtraction, cross, multiplication,
						 product, multiply, divide
"""

class CRUD:
	"""
	Class Initialization
	"""
	def __init__(self):
		self.result = 0
		self.changed = False

	def __str__(self):
		if self.changed:
			return str(self.result)
		return str('No data provided to operate')


	def set_changed(self):
		self.changed = True

	def do_oprn(self, *args, operator=None, **kwargs):
		"""
		Do operation
		i.e. operation = *, -, +, /
		"""
		self.operator = operator

		if not self.operator:
			return f'No operator provided'

		if self.operator == '+':
			return self.sum(*args, **kwargs)
		elif self.operator == '-':
			return self.subtract(*args, **kwargs)
		elif self.operator == '*':
			return self.multiple(*args, **kwargs)
		elif self.operator == '/':
			return self.division(*args, **kwargs)
		else:
			return f'Currently Operator ({operator}) is not Applicable'


	def sum(self, *args, **kwargs):
		"""
		Sum Operation
		"""
		try:
			if args:
				[int(i) for i in args]
			if kwargs:
				[int(i) for i in kwargs.values()]
		except:
			raise 'Only Integers allowed'

		for i in args:
			self.result += i

		for i in kwargs.values():
			self.result += i

		self.set_changed()
		return self


	def subtract(self, *args, **kwargs):
		"""
		Subtraction Operation
		"""
		try:
			if args:
				[int(i) for i in args]
			if kwargs:
				[int(i) for i in kwargs.values()]
		except:
			raise 'Only Integers allowed'

		for i in args:
			self.result -= i

		for i in kwargs.values():
			self.result -= i

		self.set_changed()
		return self


	def multiple(self, *args, **kwargs):
		"""
		multiplication Operation
		"""
		try:
			if args:
				[int(i) for i in args]
			if kwargs:
				[int(i) for i in kwargs.values()]
		except:
			raise 'Only Integers allowed'

		for i in args:
			self.result *= i

		for i in kwargs.values():
			self.result *= i

		self.set_changed()
		return self


	def division(self, *args, **kwargs):
		"""
		multiplication Operation
		"""
		try:
			if args:
				[int(i) for i in args]
			if kwargs:
				[int(i) for i in kwargs.values()]
		except:
			raise 'Only Integers allowed'

		for i in args:
			self.result /= i

		for i in kwargs.values():
			self.result /= i

		self.set_changed()
		return self


	# Add Alias
	# To make large chain


	# sum Aliases
	def plus(self, *args, **kwargs):
		return self.sum(*args, **kwargs)

	def addition(self, *args, **kwargs):
		return self.sum(*args, **kwargs)

	def add(self, *args, **kwargs):
		return self.sum(*args, **kwargs)


	# Subtract Aliases
	def minus(self, *args, **kwargs):
		return self.subtract(*args, **kwargs)

	def subtraction(self, *args, **kwargs):
		return self.subtract(*args, **kwargs)


	# multiply Aliases
	def cross(self, *args, **kwargs):
		return self.multiple(*args, **kwargs)

	def multiplication(self, *args, **kwargs):
		return self.multiple(*args, **kwargs)

	def product(self, *args, **kwargs):
		return self.multiple(*args, **kwargs)

	def multiply(self, *args, **kwargs):
		return self.multiple(*args, **kwargs)


	# division Aliases
	def divide(self, *args, **kwargs):
		return self.division(*args, **kwargs)
