import cmd
from tokenize import lexer
from run import evaluate
from shareds import MyLambdaErr
# import parse.parser as parse

# Constants
input_prompt = "-: "
contin_prompt = "..\t"

class LambdaConsole(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.intro = "myLambda (C) 2011 Lolcathorst\n" \
		             "Type \"help\" for more information."
		self.prompt = input_prompt
		self.env = evaluate.Environment()
		self.line = ""

	def emptyline(self):
		pass # Empty lines have no effect

	def buildParseTree(self, line):
		tokens = lexer.tokenize(line)
		###############################################################
		"""parsers = parse.parserGenerator(line)
		for p in parsers:
			# possible to open separate threads here
			p.parse()
		"""
		for t in tokens:
			print t, type(t).__name__

		###############################################################

		return None # TODO: Let there be action!

	def default(self, line):
		cmd = self.buildParseTree(line)
		if cmd is not None:
			try:
				print self.env(cmd).value
			except MyLambdaErr, e:
				print "%s: %s" % (type(e).__name__, e)

	def precmd(self, line):
		""" Buffer input unless it ends by '.' """
		ls = line.partition(';')[0].strip()
		if ls in ("", "help", "quit"):
			return ls
		if ls[-1] != '.':
			self.prompt = contin_prompt
			self.line = "%s\n%s" % (self.line, ls)
			return ""
		else:
			self.prompt = input_prompt
			dummy = self.line
			self.line = ""
			return "%s\n%s" % (dummy, ls)

	def help_quit(self):
		print "Quits the interactive console"

	def help_help(self):
		print "Type help <command> for help about <command>"

	def do_quit(self, prm):
		return True
