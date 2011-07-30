# Load a file an run the code in it 

from run import evaluate
from shareds import MyLambdaErr
from parse.parser import buildParseTree

import sys

def runscript(txt):
	env = evaluate.Environment()
	for line in filter(lambda s: s.strip(), txt.split(".")):
		for cmd in buildParseTree(line+"."):
			try:
				env(cmd)
			except MyLambdaErr, e:
				print "%s: %s" % (type(e).__name__, e)

def runfile(filename):
	try:
		f = open(filename)
		runscript(f.read())
		f.close()
	except IOError, e:
		print >> sys.stderr, "mylambda:", e

