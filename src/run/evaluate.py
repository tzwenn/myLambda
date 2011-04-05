import symbols
from builtins import BuiltIns
from run.identifiers import IdentifiersList

"""
Exception, raised if a not yet implemented symbol is evaluated.
"""
class NotImplementedError(IndexError):
	pass

class Environment(object):

	def __init__(self):
		self.identifiers = IdentifiersList()
		self.builtins = BuiltIns(self.evaluate) # TODO: Throw them up there

	"""
	THE evaluation function that actually gives life to the parse Symbols

	@param symbol	A symbol to be evaluated
	@returns	A Value or Function-Symbol representing the evaluations result (both joined into Returnable)
	"""
	def evaluate(self, symbol):
#		if not isinstance(symbol, symbols.Symbol):
#			raise ValueError, "Can only evaluate symbols."
		if isinstance(symbol, symbols.Returnable): # func or value?
			return symbol
		elif isinstance(symbol, symbols.Bind):
			return self.__evBind(symbol)
		elif isinstance(symbol, symbols.Name):
			return self.identifiers[symbol]
		elif isinstance(symbol, symbols.Call):
			return self.__evCall(symbol)
		raise NotImplementedError, "Not implemented symbol %s" % type(symbol).__name__

	def __evBind(self, symbol):
		key = self.identifiers.checkKey(symbol.name)
		res = self.evaluate(symbol.expr)
		self.identifiers.unsaveSet(key, res)
		return res

	def __evCall(self, symbol):
		func = self.evaluate(symbol.func)
		# FIXME: I assume to have a Func-Symbol
		if len(func.args) != len(symbol.args):
			raise TypeError, "Function takes exactly %d arguments (%d given)" % (len(func.args), len(symbol.args))
		self.identifiers.push()
		res = ex = None
		try:
			for i in xrange(len(func.args)):
				self.identifiers.unsaveSet(func.args[i], self.evaluate(symbol.args[i]))
			res = self.evaluate(func.dfn)
		except Exception, ex:
			self.identifiers.pop()
		self.identifiers.pop()
		if res is None:
			raise ex
		return res
