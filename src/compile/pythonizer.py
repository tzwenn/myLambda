import symbols
from compile.builtins import BuiltIns

class Pythonzier:
	""" Converts myLambda symbols to Python """

	def __init__(self):
		self.builtIns = BuiltIns(self.__tr)

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
		elif isinstance(symbol, symbols.Call):
			return self.__trCall(symbol)
		# TODO: Cex, Operator, Call
		raise NotImplementedError, "Cannot compile symbol %s yet" % type(symbol).__name__

	def __trCall(symbol):
		pass

	def __call__(self, symbol):
		return self.__tr(symbol)

