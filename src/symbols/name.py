from . import Symbol

class Name(Symbol):

	def __init__(self, name, value):
		self.name = name
		self.value = value
