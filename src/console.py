import cmd

class LambdaConsole(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "-: "
		self.intro = "myLambda (C) 2011 Lolcathorst\n" \
		             "Type \"help\" for more information."

	def emptyline(self):
		pass # Empty lines have no effect

	def default(self, line):
		pass # TODO: Let there be action!

	def help_quit(self):
		print "Quits the interactive console"

	def help_help(self):
		print "Type help <command> for help about <command>"

	def do_quit(self, prm):
		return True
