#!/usr/bin/env python3

"""
	A Simple CRUD Method Chain
"""

class CRUD:
	"""
	Class Initialization
	"""
	def __init__(self):
		self.result = None

	def __str__(self):
		return self.result


	def sign_operation(self, *args, operation=None, **kwargs):

		self.operation = operation

		if not self.operation:
			raise "Error:"

		# TODO
		if self.operation == '+':
			pass
		elif self.operation == '-':
			pass
		elif self.operation == '*':
			pass
		elif self.operation == '/':
			pass
		else:
			raise f'Currently Operation ({self.operation}) is not Applicable'



	def sum(self, *args, **kwargs):
		"""
		Sum Operation
		"""
		pass

	def subtract(self, *args, **kwargs):
		return 'mimus'

		"""
		Subtraction Operation
		"""
		pass

	def multiple(self, *args, **kwargs):
		"""
		multiplication Operation
		"""
		pass

	def division(self, *args, **kwargs):
		"""
		multiplication Operation
		"""
		pass


	# Add Alias 
	# To make large chain


	# sum Aliases
	def plus(self, *args, **kwargs):
		return self.sum(self, *args, **kwargs)

	def addition(self, *args, **kwargs):
		return self.sum(self, *args, **kwargs)

	def add(self, *args, **kwargs):
		return self.sum(self, *args, **kwargs)


	# Subtract Aliases
	def minus(self, *args, **kwargs):
		return self.subtract(self, *args, **kwargs)

	def subtraction(self, *args, **kwargs):
		return self.subtract(self, *args, **kwargs)


	# multiply Aliases
	def cross(self, *args, **kwargs):
		return self.multiple(self, *args, **kwargs)

	def multiplication(self, *args, **kwargs):
		return self.multiple(self, *args, **kwargs)

	def product(self, *args, **kwargs):
		return self.multiple(self, *args, **kwargs)

	def multiply(self, *args, **kwargs):
		return self.multiple(self, *args, **kwargs)


	# division Aliases
	def divide(self, *args, **kwargs):
		return self.division(self, *args, **kwargs)
