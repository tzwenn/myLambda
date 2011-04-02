import re

class EOFToken(object):
  pass

class BaseToken(object):
    def __init__(self, value):
        self.value = value

class IdentifierToken(BaseToken):
    def __init__(self, name):
        self.name = name

class OperatorToken(BaseToken):
    pass

class ValueToken(BaseToken): # chars later
    pass

class WhiteSpaceToken(BaseToken):
    pass

class CharacterToken(BaseToken):
    pass

# Numbers are floats and ints
NUMBER = re.compile('\d+(?:\.\d+)?')

# Can start letters and _
# at least one letter or _ is required
# ? is possible only at the end
# ++ = #x:x+1. as builtin?
IDENTIFIER = re.compile('[a-zA-Z_]+\w*[\?]{0,1}')

# check at first ( and ) and then #, = and .
BASETOKEN = re.compile('\(|\)|#\|=|\.')

# match without order
OPERATORTOKEN = re.compile('&|\||\^|\+|\-|/|%|\*{1,2}|==|>=|==|<=|!=')

COMMENT = re.compile(';.*') # not quite happy with comments after ;


def tokenize(string):
    while string:
        if string.isspace():
            yield WhiteSpaceToken()
            string = string[1:]

        comment = COMMENT.match(string).group(0)
        identifier = IDENTIFIER.match(string).group(0)
        number = NUMBER.match(string).group(0)
        baseToken = BASETOKEN.match(string).group(0)
        operatorToken = OPERATORTOKEN.match(string).group(0)

        if comment:
            string = string[len(comment):]   # skip comments

        elif identifier:
            yield IdentifierToken(identifier)
            string = string[len(identifier):]

        elif number:
            yield NumberToken(number)
            string = string[len(number):]

        elif baseToken:
            yield BaseToken(baseToken)
            string = string[len(baseToken):]

        elif operatorToken:
            yield OperatorToken(operatorToken)
            string = string[len(operatorToken):]

        else:
            yield CharacterToken(string[0])
            string = string[1:]

    yield EOFToken()
