
def isIterable(i):
	return hasattr(i,'__iter__') or hasattr(i,'__getitem__')

# ----------------------------------

class Symbol(object):
	pass

class Expr(Symbol):

	def __init__(self):
		Symbol.__init__(self)
	
class Name(Expr):

	def __init__(self, name):
		Expr.__init__(self)
		self.name = name


class Value(Expr):

	def __init__(self, value):
		Expr.__init__(self)
		if type(value) not in (int, long, float):
			raise TypeError, "Expected numeric type, but %s found" % type(value).__name__
		self.value = value
	
class Func(Expr):

	def __init__(self, args, dfn):
		Expr.__init__(self)
		if not isIterable():
			raise TypeError, "Expected iterable as list of arguments"
		if not isinstance(dfn, Expr):
			raise TypeError, "Expected expression (Expr) as definition"
		self.args = args[:]
		self.dfn = dfn