import sys
if not '../' in sys.path:    # makes common symbols accessible
    sys.path.insert(0, '..')

from tokenize.lexer import *
import symbols


class ParseError(Exception):
	pass

class Parser(object):
	"""Parses a given statement represented as token objects"""

	def __init__(self, tokens):
		self.tokens = tokens[:]
		self.result = []
		self.consumed = 0 # Tokens we've consumed
		# maybe parsed = ...

	def next(self):
		e = self.tokens[0]
		del self.tokens[0]
		self.consumed += 1
		return e

	def cutoff(self, n):
		self.tokend = self.tokens[n:]
		self.consumed += n

	def parseCall(self, exp):
		pass

	def parseName(self, t):
		"""bind or cex: first is a name, determine next token to decide"""
		for i, n in enumerate(self.tokens):
			if isinstance(n, WhiteSpaceToken):
				continue	# ignore whitespce
			if isinstance(n, BaseToken):
				if str(n) == '=':
					self.cutoff(i+1)
					return self.parseBind(t)
				elif str(n) == "(":
					pass # TODO: cex
			else:
				return t
		return t


	def parseValue(self, t):
		return t

	def parseBind(self, t):
		dump = Parser(self.tokens)
		exprTree = dump.parse()[0]		# TODO: Check list
		bindTree = symbols.Bind(t.name, exprTree)
		self.consumed += dump.consumed
		self.tokens = self.tokens[dump.consumed+1:]
		return bindTree


	def parse(self):
		"""Main method which builds the parse tree
		"""
		self.result = []
		while self.tokens:
			t = self.next()
			if isinstance(t, WhiteSpaceToken):
				continue

			# current token could be begin of a binding or call expression
			if isinstance(t, symbols.Name):
				self.result.append(self.parseName(t))

			# current token is a lambda expression
			if isinstance(t, BaseToken) and str(t) == '#':
				self.result.append(self.parseFunc(t))

			# current token is a value
			if isinstance(t, symbols.Value):
				self.result.append(self.parseValue(t))

		return self.result


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
