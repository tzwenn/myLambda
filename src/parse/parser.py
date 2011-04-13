import sys
if not '../' in sys.path:    # makes common symbols accessible
    sys.path.insert(0, '..')

import src.tokenize.lexer as lexer
import src.symbols as symbols


class Parser(object):
	"""Parses a given statement"""

	def __init__(self, stream):
		self.stream = stream

	def parseCall(self, exp):
		pass

	def parseName(self, stream):
		"""bind or cex: first is a name, determine next token to decide"""
		for i in xrange(0, len(token)):
			#skip whitespace?
			pass

	def parse(self):

		for i in xrange(0, len(stream)):

			# current token could be begin of a binding or call expression
			if isinstance(self.stream[i], symbols.Name):
				parseName(self.stream[i:])

			# current token is a lambda expression
			if isinstance(self.stream[i], symbols.BaseToken) and self.stream[i] == '#':
				parseFunc(self.stream[i:])

			# current token is a function call
			if isinstance(self.stream[i], symbols.Name) and self.stream[i+1] == '(':
				parseCall(self.stream[i:]) # skipt witespace inside

			# current token is a value
			if isinstance(self.stream[i], symbols.Value):
				parseValue(self.stream[i:])


def createStatement(tokens):
	"""create current stream of tokens
	stream is expression + '.'
	"""
	currentStream = []
	for i in xrange(0, tokens):
		current = tokens.next()
		while str(current) != '.':	# '.' marks end of statement
			currentStream.append(current)
	return currentStream	# without trailing dot

def parserGen(stream):
	"""Returns a generator parser instances for each expression
	"""
	while not isinstance(current, EOFToken):
		p = Parser(createStatement(lexer.tokenize(stream)))
		yield p

def driver():
	"""Is interface to for the repl to create fancy parser instances that behave like one object to the outside world
	"""

"""Idea: generate a parser instance for each expression an parse it in parallel
or create one parser instance which is able to parse expressions in parallel
first idea might be better because state is better encapsulated
"""




"""
Lexer Output:

# <class 'lexer.BaseToken'>
x <class 'symbols.Name'>
: <class 'lexer.CharacterToken'>
  <class 'lexer.WhiteSpaceToken'>
+ <class 'symbols.Operator'>
( <class 'lexer.BaseToken'>
x <class 'symbols.Name'>
  <class 'lexer.WhiteSpaceToken'>
1.0 <class 'symbols.Value'>
) <class 'lexer.BaseToken'>
. <class 'lexer.BaseToken'>
"""
