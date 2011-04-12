import cmd

class LambdaConsole(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "-: "

	def do_exit(self, prm):
		return True
