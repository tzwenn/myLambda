import symbols

class Pythonzier:
	""" Converts myLambda symbols to Python """

	def __init__(self):
		pass

	def __tr(self, symbol):
		if isinstance(symbol, symbols.Func):
			return "lambda %s: %s" % (", ".join(symbol.args), self.__tr(symbol.dfn))
		elif isinstance(symbol, symbols.Returnable):
			return str(symbol)
		elif isinstance(symbol, symbols.Name):
			return str(symbol)
		elif isinstance(symbol, symbols.Bind):
			# FIXME: Check if this happens global!
			return "%s = %s" % (symbol.name, self.__tr(symbol.expr))
		# TODO: Bind, Cex, Operator, Call
		raise NotImplementedError, "Cannot compile symbol %s yet" % type(symbol).__name__

	def __call__(self, symbol):
		return self.__tr(symbol)

