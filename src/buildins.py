
class BuildIns(object):
	
	def __init__(self, evaluate):
		self.__ev = evaluate
		self.__buildins = {
			'+': lambda a, b: a.value + b.value,
			'-': lambda a, b: a.value - b.value,
			'*': lambda a, b: a.value * b.value,
			'/': lambda a, b: a.value / b.value,
			'%': lambda a, b: a.value % b.value,
			'**': lambda a, b: a.value ** b.value,
			'if': lambda cond, yes, no: self.__ev(yes if cond.value else no),
		}


	def doIt(self, key, *args):
		return self.__buildins[key](*args)
