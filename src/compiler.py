#!/usr/bin/python

import sys
from parse.parser import buildParseTree
from compile.pythonizer import Pythonzier

def comp(txt, hideExceptions=True):
	py = Pythonzier()
	res = []
	thereWhereErrs = False
	for line in filter(lambda s: s.strip(), txt.split(".")):
		for cmd in buildParseTree(line+"."):
			try:
				res.append(py(cmd))
			except Exception, e:
				if hideExceptions:
					thereWhereErrs = True
					sys.stderr.write("%s: %s" % (type(e).__name__, e))
				else:
					raise
	resString = "\n".join(res)
	if hideExceptions:
		return resString, thereWhereErrs
	else:
		return resString


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		s = sys.stdin.read()
		#print "myLambda to Python: no input files"
		#sys.exit(1)
	else:
		f = open(sys.argv[1])
		s = f.read()
		f.close()
	code, errs = comp(s)
	if errs:
		sys.stderr.write("+----------------------------------------------------------+\n"
				 "|There where errors, thus the following code is incomplete.|\n"
				 "+----------------------------------------------------------+")
	print code
