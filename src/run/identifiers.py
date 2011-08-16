import symbols
from shareds import MyLambdaErr

"""
Exception to be thrown if no more contexts can be popped.
"""
class NoContextError(ValueError, MyLambdaErr):
	pass

"""
Exception, raised if a name is already bound in the current context.
"""
class NameBoundError(NameError, MyLambdaErr):
	pass

"""
Exception, raised if there is no identifier of that name in the current context.
"""
class NameUnboundError(KeyError, MyLambdaErr):
	pass

"""
Class managing all existing identifiers in different Environments instances
"""
class IdentifiersList(object):

	def __init__(self):
		self.__contexts = [{}]

	def __fitKey(self, key):
		""" If the key is a Name or Operator-symbol, get it's identifier string """
		if isinstance(key, symbols.Name):
			key = key.name
		elif isinstance(key, symbols.Operator):
			key = key.opcode
		if type(key) not in (str, unicode):
			raise TypeError, "Expected string key, but %s found" % type(key).__name__
		return key

	def __getitem__(self, key):
		key = self.__fitKey(key)
		# later defined identfiers hide away earlier ones
		#   => Start searching at end
		for context in reversed(self.__contexts):
			if key in context:
				return context[key]
		raise NameUnboundError, "Identifier '%s' not found." % key

	def checkKey(self, key):
		key = self.__fitKey(key)
		if key in self.__contexts[-1]:
			raise NameBoundError, "Identifier '%s' is already bound." % key
		return key

	def checkValue(self, value):
		if not isinstance(value, symbols.Returnable):
			raise ValueError, "Expected Value or Function to be bound to an identifer."

	def __setitem__(self, key, value):
		checkValue(value)
		self.__contexts[-1][self.checkKey(key)] = value # Only definied in most recent context

	def unsaveSet(self, key, value):
		self.__contexts[-1][key] = value

	def push(self, context=None):
		if context is None:
			self.__contexts.append({})
		else:
			self.__contexts.append(context)

	def pop(self):
		# __context[0] is global and cannot be removed
		if len(self.__contexts) == 1:
			raise NoContextError
		self.__contexts.pop()

	def dump(self):
		""" Preserve the latest context for closures """
		if len(self.__contexts) == 1:
			return {} # Global context doesn't get preserved
		# TODO: Do we want only preserve the latest context or the whole except global?
		return self.__contexts[-1]

