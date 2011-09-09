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
		raise NotImplementedError, "Cannot compile symbol %s yet" % type(symbol).__name__

