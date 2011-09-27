# BuiltIn in terms of compiling: Operators, If-Else, etc.

class BuiltIns(object):

	def __init__(self, translate):
		if not callable(translate):
			raise TypeError, "Expected callable for evaluate"
		self.__tr = translate
		self.funcs = {
			'!': lambda a: 'not (%s)' % self.__tr(a),
			'if': lambda c, a, b: '%s if %s else %s' % (self.__tr(a), self.__tr(c), self.__tr(b)),
			'print': lambda a: 'print %s' % self.__tr(a),
		}

		for op in ['!=', '*', '**', '+', '-', '/', '<', '<=', '==', '>', '>=']:
			self.funcs[op] = self.defArith(op)
		for op in ['%', '&', '^', '|']:
			self.funcs[op] = self.intArith(op)

		"""self.funcs = {

			# List functions
			'head': BuiltIn(1, self.__head),
			'tail': BuiltIn(1, lambda a: List(self.__syToLst(a)[1:])),
			'cons': BuiltIn(2, lambda h, t: List([self.__ev(h)] + self.__syToLst(t))),
			'append': BuiltIn(2, lambda a, b: List(self.__syToLst(a) + self.__syToLst(b))),
			'map': BuiltIn(2, self.__map),
			'filter': BuiltIn(2, self.__filter),
			'foldl': BuiltIn(3, self.__foldl),

			# Input/Output
			'input': BuiltIn(0, lambda: Value(float(raw_input()))),

			# Reading libs TODO: What about a search path?
			'import': BuiltIn(1, lambda s: runfile(s.name+FileExt, self.__ev)),
		}"""
	
	def defArith(self, op):
		return lambda a, b: "(%s %s %s)" % (self.__tr(a), op, self.__tr(b))

	def intArith(self, op):
		return lambda a, b: "(int(%s) %s int(%s))" % (self.__tr(a), op, self.__tr(b))
	
	def __contains__(self, func):
		return func in self.funcs.keys()

	def __call__(self, key, args):
		return self.funcs[key](*args)
