import re

class EOFToken(object):
    def __str__(self):
        return 'EOF reached'

class BaseToken(object):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class IdentifierToken(BaseToken):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class OperatorToken(BaseToken):
    pass

class ValueToken(BaseToken): # chars later
    pass

class WhiteSpaceToken(BaseToken):
    def __init__(self):
        BaseToken.__init__(self, ' ')

class CharacterToken(BaseToken):
    def __init__(self, value):
        BaseToken.__init__(self, value)

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
    """Generator to yield tokens"""

    while string:
        if string.isspace():
            yield WhiteSpaceToken()
            string = string[1:]

        comment = COMMENT.match(string)
        identifier = IDENTIFIER.match(string)
        number = NUMBER.match(string)
        baseToken = BASETOKEN.match(string)
        operatorToken = OPERATORTOKEN.match(string)

        if comment:
            comment = comment.group(0)
            string = string[len(comment):]   # skip comments

        elif identifier:
            identifier = identifier.group(0)
            yield IdentifierToken(identifier)
            string = string[len(identifier):]

        elif number:
            number = number.group(0)
            yield ValueToken(number)
            string = string[len(number):]

        elif baseToken:
            baseToken = baseToken.group(0)
            yield BaseToken(baseToken)
            string = string[len(baseToken):]

        elif operatorToken:
            operatorToken = operatorToken.group(0)
            yield OperatorToken(operatorToken)
            string = string[len(operatorToken):]

        else:
            yield CharacterToken(string[0]) # yields unknown char
            string = string[1:]

    yield EOFToken()    # we're done

