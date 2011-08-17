from tokenize.lexer import *
import symbols

class ParseError(Exception):
	pass

class Parser(object):
	"""Parses a given statement represented as token objects"""

	def __init__(self, tokens, isNested=False):
		self.tokens = tokens[:]
		self.isNested = isNested
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
		dump = Parser(self.tokens, True)
		callTree = symbols.Call(func, dump.parse(forceExpr=False))
		self.cutoff(dump.consumed)
		return callTree

	def parseName(self, t):
		"""bind or cex: first is a name, determine next token to decide"""
		if self.tokens:
			n = self.tokens[0]
			if isinstance(n, BaseToken) and str(n) == "=":
				self.next() # Cut off "="
				return self.parseBind(t)
			elif isinstance(n, BaseToken) and str(n) == "(":
				self.next() # Cut off "("
				return self.parseCall(t)
			elif isinstance(n, BaseToken) and str(n) == ")":
				return t    # Let parse() end this expr for us
		return t

	def parseOperator(self, t):
		if self.tokens:
			n = self.tokens[0]
			if isinstance(n, BaseToken) and str(n) == "(":
				self.next()
				return self.parseCall(t)
			elif isinstance(n, BaseToken) and str(n) == ")":
				return t
		return t

	def parseFunc(self, t):
		args = []
		while self.tokens:
			t = self.next()
			if isinstance(t, symbols.Name):
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

	def analyseToken(self, t, last):
		""" Find out what this token means - context free """
		# current token could be begin of a binding or call expression
		if isinstance(t, symbols.Name):
			return self.parseName(t)

		# current token is a value
		elif isinstance(t, symbols.Value):
			return self.parseValue(t)

		# taking Func here too is akward
		#but since we don't use CEX, this will do
		elif isinstance(t, symbols.Operator) or isinstance(t, symbols.Func):
			return self.parseOperator(t)

		elif isinstance(t, BaseToken):
			# current token is a lambda expression
			if str(t) == "#":
				return self.parseFunc(t)
			elif str(t) == ")":
				""" Closing brackets end an expr
				    This is not part of the grammar, but atm
				    helpfull for ending a call or cex
				"""
				if not self.isNested:
					self.consumed -= 1
				return None
			elif str(t) == "(":
				dump = Parser(self.tokens, True)
				obj = dump.parse()
				self.cutoff(dump.consumed)
				return self.analyseToken(obj, t)
			elif str(t) == "[":
				dump = Parser(self.tokens, True)
				obj = dump.parse(False)
				self.cutoff(dump.consumed)
				return symbols.List(obj)
			elif str(t) == "]":
				return None

	def parse(self, forceExpr=True): # a.k.a. parseExpr
		"""Main method which builds the parse tree
		"""
		result = []
		sym = None
		while self.tokens:
			last = sym
			sym = self.analyseToken(self.next(), last)
			if sym is None:
				break
			result.append(sym)

		if forceExpr:
			if len(result) > 1:
				raise ParseError, "End of expression expected, found \"%s\"" % str(result[1])
			elif result:
				return result[0]
			else:
				return None # TODO: Catch it
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

def buildParseTree(line):
	parsers = parserGenerator(line)
	for p in parsers:
		try:
			yield p.parse()
		except ParseError, e:
			print "%s: %s" % (type(e).__name__, e)
			break

