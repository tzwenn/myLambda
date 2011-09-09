#!/usr/bin/python

import sys
from parse.parser import buildParseTree
from compile.pythonizer import Pythonzier

def comp(txt):
	py = Pythonzier()
	for line in filter(lambda s: s.strip(), txt.split(".")):
		for cmd in buildParseTree(line+"."):
			print py(cmd)

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		s = sys.stdin.read()
		#print "myLambda to Python: no input files"
		#sys.exit(1)
	else:
		f = open(sys.argv[1])
		s = f.read()
		f.close()
	comp(s)
			
