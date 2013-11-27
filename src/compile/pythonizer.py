import symbols
from compile.builtins import BuiltIns

class Pythonzier:
	""" Converts myLambda symbols to Python """

	def __init__(self):
		self.builtIns = BuiltIns(self.__tr)

	def __tr(self, symbol):
		if type(symbol) == str:
			return symbol
		if isinstance(symbol, symbols.Func):
			return "lambda %s: %s" % (", ".join(symbol.args), self.__tr(symbol.dfn))
		elif isinstance(symbol, symbols.List):
			return "[%s]" % ", ".join(map(self.__tr, symbol.items))
		elif isinstance(symbol, symbols.Returnable):
			return str(symbol)
		elif isinstance(symbol, symbols.Name):
			return str(symbol)
		elif isinstance(symbol, symbols.Operator):
			return str(symbol)
		elif isinstance(symbol, symbols.Bind):
			# FIXME: Check if this happens global!
			return "%s = %s" % (symbol.name, self.__tr(symbol.expr))
		elif isinstance(symbol, symbols.Call):
			return self.__trCall(symbol)
		# TODO: Cex
		raise NotImplementedError, "Cannot compile symbol %s yet" % type(symbol).__name__

	def __trCall(self, symbol):
		func = self.__tr(symbol.func)
		args = map(self.__tr, symbol.args)

		if func in self.builtIns:
			return self.builtIns(func, args)
		else:
			return '%s(%s)' % (func, ", ".join(args))

	def __call__(self, symbol):
		return self.__tr(symbol)

