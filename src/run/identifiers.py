import symbols # TODO: Beautify thiz!

"""
Exception to be thrown if no more contexts can be poped.
"""
class NoContextError(ValueError):
	pass

"""
Exception, raised if a name is already bound in the current context.
"""
class NameBoundError(NameError):
	pass

"""
Exception, raised if there is no identifier of that name in the current context.
"""
class NameUnboundError(KeyError):
	pass

"""
Class managing all existing identifiers in different contexts
"""
class IdentifiersList(object):

	def __init__(self):
		self.__contexts = [{}]

	def __fitKey(self, key)
		if isinstance(key, symbols.Name):
			key = key.name
		if type(key) not in (str, unicode):
			raise TypeError, "Expected string key, but %s found" % type(key).__name__
		return key

	def __getitem__(self, key):
		key = self.__fitKey(key)
		# later defined identfiers hide away earlyer ones
		#   => Start searching at end
		for context in reversed(self.__contexts):
			if key in context:
				return context[key]
		raise NameUnboundError, "Identifier '%s' not found." % key

	def __setitem__(self, key, value):
		key = self.__fitKey(key)
		# only Value or Function accepted (can we merge that into a class?)
		if not (isinstance(value, Value) or isinstance(value, Func)):
			raise ValueError, "Expected Value or Function to be bound to an identifer."
		if key in self.__context[-1]:
			raise NameBoundError, "Identifier '%s' is already bound." % key
		self.__context[-1][key] = value # Only definied in most recent context

	def push(self):
		self.__contexts.append({})

	def pop(self):
		# __context[0] is global and cannot be removed 
		if len(self.__context) == 1:
			raise NoContextError
		self.__contexts.pop()

