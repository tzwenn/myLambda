#!/usr/bin/python

import sys
import script

if __name__ == "__main__":
	if len(sys.argv) > 1:

	else:
		from console import LambdaConsole
		cmd = LambdaConsole()
		cmd.cmdloop()

