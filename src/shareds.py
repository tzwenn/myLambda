FileExt = ".mld"
ValueTypes = (int, long, float, bool)

"""
Function for checking whether an object is iterable

@param i	object to be checked
@return A   boolean value whether i is an iterable object
"""
def isIterable(i):
	return hasattr(i,'__iter__') or hasattr(i,'__getitem__')

def toBool(value):
	return bool(value.value) if hasattr(value,"value") else (bool(value.items) if hasattr(value,"items") else false)

class MyLambdaErr(Exception):
	pass
