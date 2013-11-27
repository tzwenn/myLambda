# BuiltIn in terms of compiling: Operators, If-Else, etc.

class BuiltIns(object):

	def __init__(self, translate):
		if not callable(translate):
			raise TypeError, "Expected callable for evaluate"
		self.__tr = translate
		self.funcs = {
			'!': lambda a: 'not (%s)' % self.__tr(a),
			'if': lambda c, a, b: '%s if %s else %s' % (self.__tr(a), self.__tr(c), self.__tr(b)),

			# List functions
			'head': lambda lst: '(%s)[0]' % self.__tr(lst),
			'tail': lambda lst: '(%s)[1:]' % self.__tr(lst),
			'cons': lambda e, lst2: '[%s] + (%s)' % (self.__tr(e), self.__tr(lst2)),
			'append': lambda lst1, lst2: '(%s) + (%s)' % (self.__tr(lst1), self.__tr(lst2)),
			'map': lambda func, lst: 'map(%s, %s)' % (self.__tr(func), self.__tr(lst)),
			'filter': lambda func, lst: 'filter(%s, %s)' % (self.__tr(func), self.__tr(lst)),

			# Input/Output
			'print': lambda a: 'print %s' % self.__tr(a),
			'input': lambda: 'float(raw_input())',
		}

		for op in ['!=', '*', '**', '+', '-', '/', '<', '<=', '==', '>', '>=']:
			self.funcs[op] = self.defArith(op)
		for op in ['%', '&', '^', '|']:
			self.funcs[op] = self.intArith(op)

		"""self.funcs = {

			'foldl': BuiltIn(3, self.__foldl),


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
