import sys
if not '../' in sys.path:    # makes common symbols accessible
    sys.path.insert(0, '..')

from tokenize.lexer import *
import symbols


class ParseError(Exception):
	pass

class Parser(object):
	"""Parses a given statement represented as token objects
    """

	def __init__(self, tokens):
		self.tokens = list(tokens)
		self.pos = 0
		self.cur = self.tokens[0]
		# maybe parsed = ...

	def next(self):
		self.pos += 1
		if self.pos >= len(self.tokens):
			raise StopIteration
			return
		self.cur = self.tokens[self.pos]

	def parseCall(self, exp, result):
		pass

	def parseName(self, tokens, result):
		"""bind or cex: first is a name, determine next token to decide"""
		bindTokens = []
		cexTokens = []
		for i in xrange(len(tokens)):
			if isinstance(tokens[i], WhiteSpaceToken):
				pass	# ignore whitespce
				#tokens = tokens[:i] + tokens[i+1:]	# remove whitespace
			if str(tokens[i]) == '=':
				bindTokens.append(tokens[0])
				bindTokens.append(tokens[i])
				for i in xrange(j, len(tokens)):
					if isinstance(token[j], WhiteSpaceToken):
						pass
					bindTokens.append(parseExpression(tokens[j:]))
		if bindTokens and cexTokens:
			raise ParseError, "Can't decide whether %s is a Call Expression or a Bind" % str(tokens)


	def parseValue(self, t):
		self.tokens =  tokens[1:]		# update not yet parsed tokens
		return symbols.Value(tokens[0])

	def parseBind(self, tokens):
		pass

	def parse(self):
		"""Main method which builds the parse tree
		"""
		for t in self.tokens:
			# current token could be begin of a binding or call expression
			if isinstance(t, symbols.Name):
				self.parseName(t)

			# current token is a lambda expression
			if isinstance(t, BaseToken) and str(t) == '#':
				self.parseFunc(t)

			# current token is a function call
			if isinstance(t, symbols.Name) and self.stream[i+1] == '(':
				self.parseCall(t)

			# current token is a value
			if isinstance(t, symbols.Value):
				self.parseValue(t)


def createStatement(tokens):
	"""takes the token generator object and creates one stream of tokens
    which represent one statement without trailing '.'
	"""
	currentStream = []			# create buffer for one expression
	for t in tokens:
		if str(t) == '.':		# '.' marks end of statement
			yield currentStream
			currentStream = []
		else:
			currentStream.append(t)

def parserGenerator(string):
	"""Generator to create parser instances for each expression
	"""
	statements = createStatement(tokenize(string))
	for s in statements:
		yield Parser(s)		# call my return value with self.parse()
