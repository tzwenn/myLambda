from shareds import toBool, MyLambdaErr, FileExt
from symbols import Value, Func
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
			'+': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) + self.__syToNmb(b))),
			'-': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) - self.__syToNmb(b))),
			'*': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) * self.__syToNmb(b))),
			'/': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) / self.__syToNmb(b))),
			'%': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) % self.__syToNmb(b))),
			'**': BuiltIn(2, lambda a, b: Value(self.__syToNmb(a) ** self.__syToNmb(b))),
			'==': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) == self.__syToNmb(b))),
			'<=': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) <= self.__syToNmb(b))),
			'>=': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) >= self.__syToNmb(b))),
			'<': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) < self.__syToNmb(b))),
			'>': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) > self.__syToNmb(b))),
			'!=': BuiltIn(2, lambda a, b:  Value(self.__syToNmb(a) != self.__syToNmb(b))),
			'&': BuiltIn(2, lambda a, b:  Value(self.__syToBol(a) and self.__syToBol(b))),
			'|': BuiltIn(2, lambda a, b:  Value(self.__syToBol(a) or self.__syToBol(b))),
			'^': BuiltIn(2, lambda a, b:  Value(self.__syToBol(a) ^ self.__syToBol(b))),
			'!': BuiltIn(1, lambda a: Value(not self.__syToBol(a))),

			'print': BuiltIn(1, lambda a: (lambda val: stdout.write("%s\n" % str(val)) or val)(self.__ev(a))),
			'input': BuiltIn(0, lambda: Value(float(raw_input()))),

			#TODO: What about a search path?
			'import': BuiltIn(1, lambda s: runfile(s.name+FileExt, self.__ev)),

			'if': BuiltIn(3, lambda cond, yes, no: self.__ev(yes if self.__syToBol(cond) else no)),
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

	def __syToList(self, symbol):
		""" Returns the python list of items from a Symbol """
		lst = self.__ev(symbol)
		if not isinstace(lst, List): # Same as above
			raise WrongTypeError("Expected List, found '%s'" % type(val).__name__)
		return lst.items

	def __call__(self, key, args):
		return self.funcs[key](*args)

