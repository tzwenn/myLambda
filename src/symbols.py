import shareds

class Symbol(object):
	pass

class Expr(Symbol):

	def __init__(self):
		Symbol.__init__(self)

class Returnable:
	pass

class Callable:
	pass

class Cex(Expr):

	"""
	Constructor that creates a callable Expression.
	This is a FORWARD (!!!) for \(expr\) etc

	@param expr	Expression that we are forwarded to
	"""
	def __init__(self, expr):
		Expr.__init__(self)
		if isinstance(expr, Expr):
			raise TypeError, "Expected expression"
		self.expr = expr

class Name(Expr):

	"""holds a value which means a number"""
	def __init__(self, name):
		Expr.__init__(self)
		if type(name) not in (unicode, str):
			raise TypeError, "Expected string type, but %s found" % type(value).__name__
		self.name = name

	def __str__(self):
		return self.name


class Bind(Expr):

	"""
	Constructor that creates a bind symbol

	@param name	String value for the identifyer
	@param bind	Expression symbol that we'd liked to be bound to
	"""
	def __init__(self, name, expr):
		Expr.__init__(self)
		if type(name) not in (unicode, str):
			raise TypeError, "Excpected string type, but %s found" % type(name).__name__
		if not isinstance(expr, Expr):
			raise TypeError, "Expected expression"
		self.name = name
		self.expr = expr

class Value(Expr, Returnable):

	"""
	Constructor that creates a value symbol which are currently numbers only

	@param value	Numeric value represented by this symbol
	"""
	def __init__(self, value):
		Expr.__init__(self)
		if type(value) not in shareds.ValueTypes:
			raise TypeError, "Expected numeric type, but %s found" % type(value).__name__
		self.value = value

	def __str__(self):
		return str(self.value)

class List(Expr, Returnable):

	"""
	Constructor that creates a list symbol

	@param items	List of symbols representing the items of the list
	"""
	def __init__(self, items):
		Expr.__init__(self)
		if not shareds.isIterable(items):
			raise TypeError, "Expected list to be created from iterable"
		self.items = items

	def __str__(self):
		return "[%s]" % " ".join(map(str, self.items))
		

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
		self.argc = len(args)
		self.dfn = dfn
		self.cscope = None	# Creation scope

	def __str__(self):
		return "<function/%d>" % self.argc

class Operator(Expr, Callable): # TODO: Change that!
	"""holds builtin functions like basic math, logic and bit manipulation"""

	def __init__(self, opcode):
		self.opcode = opcode

	def __str__(self):
		return self.opcode

class Call(Expr):

	def __init__(self, func, args):
		Expr.__init__(self)
		if not shareds.isIterable(args):
			raise TypeError, "Expected iterable as list of arguments"
		for i, arg in enumerate(args):
			if not isinstance(args[i], Expr):
				raise TypeError, "Argument %d is no expression" % (i + 1)
		self.func = func
		self.args = args

