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



class IdentifiersList(object):

	def __init__(self):
		self.__contexts = [{}]

	def __getitem__(self, key):
		if isinstance(key, symbols.Name):
			key = key.name
		if type(key) not in (str, unicode):
			raise TypeError, "Expected string key, but %s found" % type(key).__name__
		for context in reversed(self.__contexts):
			if key in context:
				return context[key]
		raise NameUnboundError, "Identifier '%s' not found." % key

	def __setitem__(self, key, value):
		pass

	def push(self):
		self.__contexts.append({})

	def pop(self):
		self.__contexts.pop()
