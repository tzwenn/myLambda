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
		self.builtins = BuiltIns(self.evaluate) # TODO: Throw them up there

	"""
	THE evluation function that actually gives live to the parse Symbols

	@param symbol	A symbol to be evaluated
	@returns	A Value or Function-Symbol representing the evaluations result (both joined into Returnable)
	"""
	def evaluate(self, symbol):
#		if not isinstance(symbol, symbols.Symbol):
#			raise ValueError, "Can only evaluate symbols."
		if isinstance(symbol, symbols.Returnable): # func or value?
			return symbol
		if isinstance(symbol, symbold.Bind):
			key = self.identifiers.checkKey(symbol.name)
			res = self.evaluate(symbol.expr)
			self.identifiers.unsaveSet(key, res)
			return res
		raise NotImplementedError, "Not implemented symbol %s" % type(symbol).__name__

