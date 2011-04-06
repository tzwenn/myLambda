#TODO:	Convert to a function (?) returning a dictionary given an __ev-function.
#	Decorator possible?

from shareds import toBool
from symbols import Value, Func

class BuiltIn(Func):

	def __init__(self, argc, dfn):
		self.argc = argc
		self.dfn = dfn

	def __call__(self, *args):
		return self.dfn(*args)

class BuiltIns(object):

	def __init__(self, evaluate):
		if not callable(evaluate):
			raise TypeError, "Expected callable for evaluate"
		self.__ev = evaluate
		self.funcs = {
			'+': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) + self.__syToNmb(b))),
			'-': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) - self.__syToNmb(b))),
			'*': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) * self.__syToNmb(b))),
			'/': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) / self.__syToNmb(b))),
			'%': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) % self.__syToNmb(b))),
			'**': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) ** self.__syToNmb(b))),
			'==': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) == self.__syToNmb(b))),
			'if': BuiltIn(3, lambda cond, yes, no: self.__ev(yes if toBool(self.__ev(cond)) else no)),
		}

	def __syToNmb(self, symbol):
		"""Symbol to numeric value"""
		return self.__ev(symbol).value


	def doIt(self, key, *args):
		return self.funcs[key](*args)

	def __call__(self, key, *args):
		return doIt(key, args)

