import sys
if not '../' in sys.path:    # makes common symbols accessible
    sys.path.insert(0, '..')

import src.tokenize.lexer as lexer
import src.symbols as symbols


class Parser(object):
	"""Parses a given statement represented as token objects
    """

	def __init__(self, tokens):
		self.tokens = tokens

	def parseCall(self, exp):
		pass

	def parseName(self, tokens):
		"""bind or cex: first is a name, determine next token to decide"""
		#for i in xrange(0, len(token)):
			#skip whitespace?
		pass

	def parse(self):
		"""Main method which builds the parse tree
		"""
		#list(t for t in self.tokens)
		#for i in xrange(0, len(stream)):

		for t in self.tokens:
			# current token could be begin of a binding or call expression
			if isinstance(t, symbols.Name):
				self.parseName()

			# current token is a lambda expression
			if isinstance(t, symbols.BaseToken) and str(t) == '#':
				self.parseFunc()

			# current token is a function call
			if isinstance(t, symbols.Name) and self.stream[i+1] == '(':
				self.parseCall()

			# current token is a value
			if isinstance(t, symbols.Value):
				self.parseValue()


def createStatement(tokens):
	"""takes the token generator object and creates one stream of tokens 
    which represent one statement without trailing '.'
	"""
	currentStream = []
	for t in tokens:
		current = tokens.next()
		while str(current) != '.':	# '.' marks end of statement
			currentStream.append(current)
			current = tokens.next()
		yield currentStream

def parserGenerator(string):
	"""Generator to create parser instances for each expression
	"""
	statements = createStatement(lexer.tokenize(string))
	for s in statements:
		yield Parser(s) 	# call my return value with self.parse()
