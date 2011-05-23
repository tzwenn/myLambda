#import src.symbols as symbols
import symbols
import shareds

class ParseError(shareds.MyLambdaErr):
	pass

class P(object):
	def __init__(self):
		pass

	def parse(self, tokens):
		result = []
		for i in xrange(0, list(tokens)):
			if str(tokens[i]) != '.':
				print tokens[i].__class__, "11"

				# it's just a number
				if isinstance(tokens[i], symbols.Value):
					return tokens[i]	# already parsed Number in lexer.py

				# maybe it's a name
				elif isinstance(tokens[i], symbols.Name):
					curr = tokens[i+1]
					if str(curr) == '=':
						if isinstance(tokens[i+2], symbols.Value):
							return symbols.Bind([Name(tokens[i]), tokens[i+2]])
				else:
					raise ParseError, "Only numbers are allowed" # TODO catch me if you can

