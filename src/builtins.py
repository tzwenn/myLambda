from shareds import toBool, MyLambdaErr, FileExt
from symbols import Value, Func, List
from sys import stdout
from script import runfile

class WrongTypeError(TypeError, MyLambdaErr):
	pass

class BuiltIn(Func):

	def __init__(self, argc, dfn):
		self.argc = argc
		self.dfn = dfn

	def __call__(self, args):
		return self.dfn(*args)

class BuiltIns(object):

	def __init__(self, evaluate):
		if not callable(evaluate):
			raise TypeError, "Expected callable for evaluate"
		self.__ev = evaluate
		self.funcs = {
			# Arithmetic
			'+': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) + self.__syToNmb(b))),
			'-': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) - self.__syToNmb(b))),
			'*': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) * self.__syToNmb(b))),
			'/': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) / self.__syToNmb(b))),
			'%': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) % self.__syToNmb(b))),
			'**': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) ** self.__syToNmb(b))),

			# Comparison
			'==': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) == self.__syToNmb(b))),
			'<=': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) <= self.__syToNmb(b))),
			'>=': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) >= self.__syToNmb(b))),
			'<': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) < self.__syToNmb(b))),
			'>': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) > self.__syToNmb(b))),
			'!=': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) != self.__syToNmb(b))),

			# Boolean algebra
			'&': BuiltIn(2, lambda a, b:  Value(self.__syToBol(a) and self.__syToBol(b))),
			'|': BuiltIn(2, lambda a, b:  Value(self.__syToBol(a) or self.__syToBol(b))),
			'^': BuiltIn(2, lambda a, b:  Value(self.__syToBol(a) ^ self.__syToBol(b))),
			'!': BuiltIn(1, lambda a: Value(not self.__syToBol(a))),

			# List functions
			'head': BuiltIn(1, self.__head),
			'tail': BuiltIn(1, lambda a: List(self.__syToLst(a)[1:])),
			'cons': BuiltIn(2, lambda a, b: List([self.__ev(a)] + self.__syToLst(b))),

			# Input/Output
			'input': BuiltIn(0, lambda: Value(float(raw_input()))),
			'print': BuiltIn(1, lambda a: (lambda val: stdout.write("%s\n" % str(val)) or val)(self.__ev(a))),

			# Conditional evaluation 
			'if': BuiltIn(3, lambda cond, yes, no: self.__ev(yes if self.__syToBol(cond) else no)),

			# Reading libs TODO: What about a search path?
			'import': BuiltIn(1, lambda s: runfile(s.name+FileExt, self.__ev)),
		}

	def __syToNmb(self, symbol):
		"""Symbol to numeric value"""
		val = self.__ev(symbol)
		if not isinstance(val, Value): # TODO: Nice to know who throws that
			raise WrongTypeError("Expected numeric value, found '%s'" % type(val).__name__)
		return val.value

	def __syToBol(self, symbol):
		"""Symbol to boolean value"""
		return toBool(self.__ev(symbol))

	def __syToLst(self, symbol):
		""" Returns the python list of items from a Symbol """
		lst = self.__ev(symbol)
		if not isinstance(lst, List): # Same as above
			raise WrongTypeError("Expected List, found '%s'" % type(val).__name__)
		return lst.items

	def __head(self, listSymbol):
		items = self.__syToLst(listSymbol)
		if not len(items):
			raise WrongTypeError("Cannot get head of an empty list")
		return items[0]

	def __call__(self, key, args):
		return self.funcs[key](*args)
