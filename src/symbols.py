import shareds

class Symbol(object):
	pass

class Expr(Symbol):

	def __init__(self):
		Symbol.__init__(self)

class Returnable:
	pass

class Callable: # FIXME !!!!!!!!!!!!!!!!!!!!!!!!! we need Cex (see grammar.txt)
	pass

class Name(Expr):

	def __init__(self, name):
		Expr.__init__(self)
		if type(name) not in (unicode, str):
			raise TypeError, "Expected string type, but %s found" % type(value).__name__
		self.name = name

class Bind(Expr):

	"""
	Contructor that creates a bind symbol

	@param name	String value for the identifyer
	@param bind	Expression symbol that we'd liked to be bound to
	"""
	def __init__(self, name, expr):
		Expr.__init__(self)
		if type(name) not in (unicode, str):
			raise TypeError, "Excpected string type, but %s found" % type(value).__name__
		if not isinstance(expr, Expr):
			raise TypeError, "Expected expression"
		self.name = name
		self.expr = expr

class Value(Expr, Returnable):

	"""
	Constructor that creates a value symbol

	@param value	Numeric value represented by this symbol
	"""
	def __init__(self, value):
		Expr.__init__(self)
		if type(value) not in shareds.ValueTypes:
			raise TypeError, "Expected numeric type, but %s found" % type(value).__name__
		self.value = value

class Func(Expr, Returnable, Callable):

	"""
	Constructor that creates a function symbol

	@param args	List of strings(!) representing the arguments
	@param dfn	Expression symbol representing the functions definition
	"""
	def __init__(self, args, dfn):
		Expr.__init__(self)
		if not shareds.isIterable(args):
			raise TypeError, "Expected iterable as list of arguments"
		for i in xrange(len(args)):
			if type(args[i]) not in (unicode, str):
				raise TypeError, "Name of parameter %d is no string" % (i + 1)
		if not isinstance(dfn, Expr):
			raise TypeError, "Expected expression (Expr) as definition"
		self.args = args[:]
		self.dfn = dfn

class Operator(Expr, Returnable, Callable): # TODO: Change that!

	def __init__(self, opcode):
		self.opcode = opcode

class Call(Expr):

	def __init__(self, func, args):
		Expr.__init__(self)
		#if not isinstance(func, Callable):
		#	raise TypeError, "Expect functions or operators to be called"
		if not shareds.isIterable(args):
			raise TypeError, "Expected iterable as list of arguments"
		for i in xrange(len(args)):
			if not isinstance(args[i], Expr):
				raise TypeError, "Argument %d is no expression" % (i + 1)
		self.func = func
		self.args = args
