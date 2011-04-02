import lexer

string = """(3**abc)&7 != 5 ; comment
        5+4  """

print tokenize
dir(tokenize)
tokens = lexer.tokenize(string)

for t in tokens:
    print t
