#TODO:	Convert to a function (?) returning a dictionary given an __ev-function. 
#	Decorator possible?

import shareds

class BuildIns(object):
	
	def __init__(self, evaluate):
		self.__ev = evaluate
		self.__buildins = {
			'+': lambda a, b: self.__ev(a) + self.__ev(b),
			'-': lambda a, b: self.__ev(a) - self.__ev(b),
			'*': lambda a, b: self.__ev(a) * self.__ev(b),
			'/': lambda a, b: self.__ev(a) / self.__ev(b),
			'%': lambda a, b: self.__ev(a) % self.__ev(b),
			'**': lambda a, b: self.__ev(a) ** self.__ev(b),
			'if': lambda cond, yes, no: self.__ev(yes if toBool(self.__ev(cond)) else no),
		}


	def doIt(self, key, *args):
		return self.__buildins[key](*args)
