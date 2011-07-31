# Load a file an run the code in it 

from shareds import MyLambdaErr
from parse.parser import buildParseTree

import sys

def runscript(txt, ev):
	for line in filter(lambda s: s.strip(), txt.split(".")):
		for cmd in buildParseTree(line+"."):
			try:
				ev(cmd)
			except MyLambdaErr, e:
				print "%s: %s" % (type(e).__name__, e)
	return True

def runfile(filename, ev):
	try:
		f = open(filename)
		runscript(f.read(), ev)
		f.close()
		return True
	except IOError, e:
		print >> sys.stderr, "mylambda:", e
		return False

