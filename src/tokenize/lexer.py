import re

class EOFToken(object):
  pass

class BaseToken(object):
    def __init__(self, value):
        self.value = value

class IdentifierToken(object):
    def __init__(self, name):
        self.name = name

class OperatorToken(object):
    def __init__(self, value):
        self.value = value

def ValueToken(self, value): # chars later
    self.value = value

# Numbers are floats and ints
NUMBER = re.compile('\d+(?:\.\d+)?')

# Can start letters and _
# at least one letter or _ is required
# ? is possible only at the end
IDENTIFIER = re.compile('[a-zA-Z_]+\w*[\?]{0,1}')

# check at first ( and ) and then #, = and .
BASETOKEN = re.compile('\(|\)|#\|=|\.')

# match without order
OPERATORTOKEN = re.compile('&|\||\^|\+|\-|/|%|\*{1,2}|==|>=|==|<=|!=')



# note to myself: wenn whitespace, nächsten Durchlauf
# Definition von ++ = #x:x+1. sollte auch gültig sein, als builtin?
