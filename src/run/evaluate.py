import symbols
from builtins import BuiltIns, BuiltIn
from run.identifiers import IdentifiersList
from shareds import MyLambdaErr

"""
Exception, raised if a not yet implemented symbol is evaluated.
"""
class NoSystemError(IndexError, MyLambdaErr):
	pass

class ArgumentError(TypeError, MyLambdaErr):
	pass

class CallError(TypeError, MyLambdaErr):
	pass

class Environment(object):

	def __init__(self):
		self.identifiers = IdentifiersList()
		self.builtins = BuiltIns(self.evaluate)
		for key, dfn in self.builtins.funcs.iteritems():
			self.identifiers.unsaveSet(key, dfn)

	"""
	THE evaluation function that actually gives life to the parse Symbols

	@param symbol	A symbol to be evaluated
	@returns	A Value or Function-Symbol representing the evaluations result (both joined into Returnable)
	"""
	def evaluate(self, symbol):
		if isinstance(symbol, symbols.Func):
			return self.__evFunc(symbol)
		elif isinstance(symbol, symbols.List):
			return symbols.List(map(self.evaluate, symbol.items))
		elif isinstance(symbol, symbols.Returnable):
			return symbol
		elif isinstance(symbol, symbols.Cex):
			return self.evaluate(symbol.expr)
		elif isinstance(symbol, symbols.Bind):
			return self.__evBind(symbol)
		elif isinstance(symbol, symbols.Name):
			return self.identifiers[symbol]
		elif isinstance(symbol, symbols.Operator):
			return self.identifiers[symbol]
		elif isinstance(symbol, symbols.Call):
			return self.__evCall(symbol)
		raise NotImplementedError, "Not implemented symbol %s" % type(symbol).__name__

	def __evFunc(self, symbol): # Called on definition of a function
		symbol.cscope = self.identifiers.dump()
		return symbol

	def __evBind(self, symbol):
		key = self.identifiers.checkKey(symbol.name)
		res = self.evaluate(symbol.expr)
		self.identifiers.unsaveSet(key, res)
		return res

	def __evCall(self, symbol):
		func = self.evaluate(symbol.func)
		if not isinstance(func, symbols.Callable):
			raise CallError, "Symbol not callable"
		if func.argc != len(symbol.args):
			raise ArgumentError, "Function takes exactly %d arguments (%d given)" % (func.argc, len(symbol.args))
		if isinstance(func, BuiltIn):
			return func(symbol.args)

		# The args going to be passed
		args = map(self.evaluate, symbol.args)

		# Only symbol.Func from here on => we know func.csope exists
		self.identifiers.push(func.cscope)
		res = ex = None
		try:
			for i in xrange(len(func.args)):
				self.identifiers.unsaveSet(func.args[i], args[i])
			res = self.evaluate(func.dfn)
		except Exception, ex:
			pass
		self.identifiers.pop()
		if res is None:
			raise ex
		return res

	def __call__(self, symbol):
		return self.evaluate(symbol)

