#TODO:	Convert to a function (?) returning a dictionary given an __ev-function.
#	Decorator possible?

import shareds
from symbols import Value

class BuiltIns(object):

	def __init__(self, evaluate):
		if not callable(evaluate):
			raise TypeError, "Expected callable for evaluate"
		self.__ev = evaluate
		self.__builtins = {
			'+': lambda a, b: Value(self.__syToNmb(a) + self.__syToNmb(b)),
			'-': lambda a, b: Value(self.__syToNmb(a) - self.__syToNmb(b)),
			'*': lambda a, b: Value(self.__syToNmb(a) * self.__syToNmb(b)),
			'/': lambda a, b: Value(self.__syToNmb(a) / self.__syToNmb(b)),
			'%': lambda a, b: Value(self.__syToNmb(a) % self.__syToNmb(b)),
			'**': lambda a, b: Value(self.__syToNmb(a) ** self.__syToNmb(b)),
			'if': lambda cond, yes, no: self.__ev(yes if toBool(self.__ev(cond)) else no),
		}

	def __syToNmb(self, symbol):
		"""Symbol to numeric value"""
		return self.__ev(symbol).value


	def doIt(self, key, *args):
		return self.__builtins[key](*args)

	def __call__(self, key, *args):
		return doIt(key, args)

