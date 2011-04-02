"""
Exception to be thrown if no more contexts can be poped.
"""
class NoContextError(ValueError):
	pass


class NameBoundError(NameError):
	pass

class NameUnboundError(NameError):
	pass

class IdentifiersList(object):

	def __init__(self):
		self.__idents = [{}]
