import lexer

# a small tokenizer loop
def go(string):
    while True:
        tokens = lexer.tokenize(string)
        for t in tokens:
            print t, t.__class__

        # entering loop
        print '>',      # hold cursor in current line
        try:
            string = raw_input()
        except KeyboardInterrupt:   # exit with ctrl+c
            return


print 'I show you an example:'
go("""& (!= (** (3 abc) 7) 5) ; comment
#x: +(x 1)""")
# as you can see newline ends a comment

