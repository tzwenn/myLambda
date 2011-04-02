import symbols
from builtins import BuiltIns
from run import identifiers

"""
Exception, raised if a not yet implemented symbol is evaluated.
"""
class NotImplementedError(IndexError):
	pass

class Evironment(object):

	def __init__(self):
		self.identifiers = indentifiers.IdentifiersList()
		self.builtins = BuiltIns(self.evaluate)

	def evaluate(self, symbol):
		if not isinstance(symbol, symbols.Symbol):
			raise ValueError, "Can only evaluate symbols."
		raise NotImplementedError, "Not implemented symbol %s" % type(symbol).__name__
