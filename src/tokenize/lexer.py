import symbols
import re

class EOFToken(object):
	"""marks end of a given input"""
	def __str__(self):
		return 'EOF'

class BaseToken(object):
	"""holds everything we need for a lambda expression or list  # : = ( ) . [ ]"""
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value

class IdentifierToken(BaseToken):
	"""holds references to lambda expressions or builtin functions"""
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return self.name

class WhiteSpaceToken(BaseToken):
	"""holds one whitespace char"""
	def __init__(self):
		BaseToken.__init__(self, ' ')

class CharacterToken(BaseToken):
	"""is used for every other ASCII input other which isn't recognized as one of the other tokens
	that means in case of #x: +(x 1).! it will hold the !"""
	def __init__(self, value):
		BaseToken.__init__(self, value)

# Numbers are floats and ints
NUMBER = re.compile('\d+(?:\.\d+)?')

# Can start with letters and _
# at least one letter or _ is required at the beginning of each identifier
# ? is possible only at the end
NAME = re.compile('[a-zA-Z_]+\w*[\?]?')

# check at first ( and ) and then #, = and .
BASETOKEN = re.compile('\(|\)|#|=|\.|\[|\]')

# builtin functions
OPERATOR = re.compile('>=|==|<=|!=|!|&|\||\^|\+|\-|/|%|<|\>|\*{1,2}')

COMMENT = re.compile(';.*') # ignore everything after a comment
							# not quite happy with comments after ;

# find all whitespaces, including formfeed and vertical tab
WHITESPACE = re.compile('\s+')

def tokenize(string):
	"""Generator to yield tokens
	usage:
	tokens = lexer.tokenize(myString)
	for t in tokens:
		print t

	for more infos have a look at src/tokenize/lexerText.py
	"""

	while string:

		comment = COMMENT.match(string)
		name = NAME.match(string)
		number = NUMBER.match(string)
		operator = OPERATOR.match(string)
		baseToken = BASETOKEN.match(string)
		whitespace = WHITESPACE.match(string)

		if comment:
			comment = comment.group(0)
			string = string[len(comment):]	 # skip comments

		elif name:
			name = name.group(0)
			yield symbols.Name(name)
			string = string[len(name):]

		elif number:
			number = number.group(0)
			yield symbols.Value(float(number))
			string = string[len(number):]

		elif operator:
			operator = operator.group(0)
			yield symbols.Operator(operator)
			string = string[len(operator):]

		elif baseToken:
			baseToken = baseToken.group(0)
			yield BaseToken(baseToken)
			string = string[len(baseToken):]

		elif whitespace:
			whitespace = whitespace.group(0)
			string = string[len(whitespace):]	# skip whitespace

		else:
			yield CharacterToken(string[0]) # yields unknown char
			string = string[1:]

	yield EOFToken()	# we're done
