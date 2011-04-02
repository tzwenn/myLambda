import shareds

class Symbol(object):
	pass

class Expr(Symbol):

	def __init__(self):
		Symbol.__init__(self)
	
class Name(Expr):

	def __init__(self, name):
		Expr.__init__(self)
		if type(value) not in (unicode, str):
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
		if type(value) not in (unicode, str):
			raise TypeError, "Excpected string type, but %s found" % type(value).__name__
		if not isinstance(expr, Expr):
			raise TypeError, "Expected expression" 
		self.name = name
		self.expr = expr


class Value(Expr):

	"""
	Constructor that creates a value symbol

	@param value	Numeric value represented by this symbol
	"""
	def __init__(self, value):
		Expr.__init__(self)
		if type(value) not in shareds.ValueTypes:
			raise TypeError, "Expected numeric type, but %s found" % type(value).__name__
		self.value = value
	
class Func(Expr):

	"""
	Constructor that creates a function symbol

	@param args	List of strings(!) representing the arguments
	@param dfn	Expression symbol representing the functions definition
	"""
	def __init__(self, args, dfn):
		Expr.__init__(self)
		if not shareds.isIterable(args):
			raise TypeError, "Expected iterable as list of arguments"
		if not isinstance(dfn, Expr):
			raise TypeError, "Expected expression (Expr) as definition"
		self.args = args[:]
		self.dfn = dfn

