import sys
if not '../' in sys.path:    # makes common symbols accessible
    sys.path.insert(0, '..')

import src.tokenize.lexer as lexer
import src.shareds as shareds
import src.symbols as symbols

import pdb


class ParseError(shareds.MyLambdaErr):
	pass


class Parser(object):
	"""Parses a given statement represented as token objects
    """

	def __init__(self, tokens):
		self.tokens = list(tokens)	#convert generator to list
		# maybe parsed = ...

	def parseCall(self, exp, result):
		pass

	def parseName(self, tokens, result):
		"""bind or cex: first is a name, determine next token to decide"""
		bindTokens = []
		cexTokens = []
		for i in xrange(0, len(tokens)):
			if isinstance(tokens[i], WhiteSpaceToken):
				pass	# ignore whitespce
				#tokens = tokens[:i] + tokens[i+1:]	# remove whitespace
			if str(tokens[i]) == '=':
				bindTokens.append(tokens[0])
				bindTokens.append(tokens[i])
				for i in xrange(j, len(tokens)):
					if isinstance(token[j], WhiteSpaceToken):
						pass
					bindTokens.append(parseExpression(tokens[j:]))	# create Bind oder so, irgendie quatsch

		if bindTokens and cexTokens:
			raise ParseError, "Can't decide whether %s is a Call Expression or a Bind" % str(tokens)


	def parseBind(self, tokens):
		pass

	def parseRec(self, tokens, prevToken):
		"""Does the recursive parsing, stops at closing brackets and
		returns the tree to the environment"""
		pass

	def parse(self):
		"""Main method which coordinates the building of the parse tree
		"""
		for t in self.tokens:
			# current token could be begin of a binding or call expression
			"""if isinstance(t, symbols.Name):
				return self.parseName(t)

			# current token is a lambda expression
			if isinstance(t, symbols.BaseToken) and str(t) == '#':
				return self.parseFunc()

			# current token is a function call
			if isinstance(t, symbols.Name) and self.stream[i+1] == '(':
				return self.parseCall()
			"""
			# current token is a value
			if isinstance(t, symbols.Value):
				return t
			#pdb.set_trace()
		return self.tokens

def createStatement(tokens):
	"""takes the token generator object and creates one stream of tokens
    which represent one statement without trailing '.'
	"""
	currentStream = []			# create buffer for one expression
	for current in tokens:
		if str(current) != '.':
			currentStream.append(current)
		else:
			if not currentStream:
				raise ParseError
			yield currentStream
			currentStream = []

def parserGenerator(string):
	"""Generator to create parser instances for each statement
	call my return value with self.parse()
	"""
	statements = createStatement(lexer.tokenize(string))
	for s in statements:
		print "I am the statement", map(str, s)
		yield Parser(s)
