import symbols
from buildins import BuildIns
from run import identifiers

class Evironment(object):

	def __init__(self):
		self.identifiers = indentifiers.IdentifiersList()
		self.buildins = BuildIns(self.evaluate)

	def evaluate(self):
		pass
