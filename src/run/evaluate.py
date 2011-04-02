import symbols
from builtins import BuiltIns
from run import identifiers

class Evironment(object):

	def __init__(self):
		self.identifiers = indentifiers.IdentifiersList()
		self.builtins = BuiltIns(self.evaluate)

	def evaluate(self):
		pass
