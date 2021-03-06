import sys
if not '../' in sys.path:	 # makes common symbols accessible
	sys.path.insert(0, '..')

import lexer

# a small tokenizer loop
def go(string):
	while True:
		tokens = lexer.tokenize(string)
		for t in tokens:
			print t, t.__class__

		# entering loop
		print '>',		# hold cursor in current line
		try:
			string = raw_input()
		except KeyboardInterrupt:	# exit with ctrl+c
			return


print 'I show you an example:'
go("""& (!= (** (3 abc) 7) 5) ; comment
#x: +(x 1)""")
print go("""hi				  d
""")
# as you can see newline ends a comment and thanks to Patrick it works for multiple whitespaces too
