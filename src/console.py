import cmd
from run import evaluate
from shareds import MyLambdaErr

class LambdaConsole(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.intro = "myLambda (C) 2011 Lolcathorst\n" \
		             "Type \"help\" for more information."
		self.prompt = "-: "
		self.env = evaluate.Environment()

	def emptyline(self):
		pass # Empty lines have no effect

	def buildParseTree(self, line):
		return None # TODO: Let there be action!

	def default(self, line):
		cmd = self.buildParseTree(line)
		if cmd is not None:
			try:
				print self.env(cmd).value
			except MyLambdaErr, e:
				print "%s: %s" % (type(e).__name__, e)


	def help_quit(self):
		print "Quits the interactive console"

	def help_help(self):
		print "Type help <command> for help about <command>"

	def do_quit(self, prm):
		return True
