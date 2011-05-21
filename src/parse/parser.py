from tokenize.lexer import *
import symbols


class ParseError(Exception):
	pass

class Parser(object):
	"""Parses a given statement represented as token objects"""

	def __init__(self, tokens):
		self.tokens = tokens[:]
		self.consumed = 0 # Tokens we've consumed
		# maybe parsed = ...

	def next(self):
		e = self.tokens[0]
		del self.tokens[0]
		self.consumed += 1
		return e

	def cutoff(self, n):
		self.tokens = self.tokens[n:]
		self.consumed += n

	def parseCall(self, func):
		dump = Parser(self.tokens)
		callTree = symbols.Call(func, dump.parse(forceExpr=False))
		self.cutoff(dump.consumed)
		return callTree

	def parseName(self, t):
		"""bind or cex: first is a name, determine next token to decide"""
		for i, n in enumerate(self.tokens):
			if isinstance(n, WhiteSpaceToken):
				continue	# ignore whitespce
			elif isinstance(n, BaseToken) and str(n) == "=":
				self.cutoff(i + 1) # Cut off whitespace + "="
				return self.parseBind(t)
			elif isinstance(n, BaseToken) and str(n) == "(":
				self.cutoff(i + 1)
				return self.parseCall(t)
			elif isinstance(n, BaseToken) and str(n) == ")":
				self.cutoff(i)
				return t
			else:
				raise ParseError, "Bind or call expected, found \"%s\"" % str(n)
		return t

	def parseFunc(self, t):
		args = []
		while self.tokens:
			t = self.next()
			if isinstance(t, WhiteSpaceToken):
				continue
			elif isinstance(t, symbols.Name):
				args.append(t.name)
			elif isinstance(t, BaseToken) and str(t) == ":":
				dump = Parser(self.tokens)
				funcTree = symbols.Func(args, dump.parse())
				self.cutoff(dump.consumed)
				return funcTree				
			else:
				raise ParseError, "Identifier or \":\" expected, found \"%s\"" % str(t)

	def parseValue(self, t):
		return t

	def parseBind(self, t):
		dump = Parser(self.tokens)
		bindTree = symbols.Bind(t.name, dump.parse())
		self.cutoff(dump.consumed)
		return bindTree


	def parse(self, forceExpr=True): # a.k.a. parseExpr
		"""Main method which builds the parse tree
		"""
		result = []
		while self.tokens:
			t = self.next()
			if isinstance(t, WhiteSpaceToken):
				continue

			# current token could be begin of a binding or call expression
			if isinstance(t, symbols.Name):
				result.append(self.parseName(t))

			# current token is a value
			if isinstance(t, symbols.Value):
				result.append(self.parseValue(t))

			if isinstance(t, BaseToken):
				# current token is a lambda expression
				if str(t) == "#": 
					result.append(self.parseFunc(t))
				elif str(t) == ")":
					""" Closing brackets end an expr
					    This is not part of the grammar, but atm
					    helpfull for ending a call or cex
					"""
					break # TODO: assert matching "(" exists

		if forceExpr:
			if len(result) > 1:
				raise ParseError, "End of expression expected, found \"%s\"" % str(self.result[1])
			else:
				return result[0]
		return result


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
