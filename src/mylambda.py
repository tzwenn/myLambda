#!/usr/bin/python

import sys

if __name__ == "__main__":
	if len(sys.argv) > 1:
		import script
		from run.evaluate import Environment
		script.runfile(sys.argv[1], Environment())
	else:
		import console
		cmd = console.LambdaConsole()
		cmd.cmdloop()

