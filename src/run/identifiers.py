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
class NameUnboundError(IndexError):
	pass

class IdentifiersList(object):

	def __init__(self):
		self.__idents = [{}]

	def __getitem__(self):
		pass
