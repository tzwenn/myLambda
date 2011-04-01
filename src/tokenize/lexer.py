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
NUMBER = re.compile('[0-9]+(?:\.[0-9]+)?')

# Can start with numbers but at least one letter or [_!|?] is required
# everythng which is not another token should be allowed
IDENTIFIER = re.compile('(\w*[a-zA-Z]|(\w^\d)+)(!|\?)?$') # not perfect

# check at first ( and ) and then #, = and .
BASETOKEN = re.compile('\(|\)|#\|=|\.')

# match without order
OPERATORTOKEN = re.compile('&|\||\^|\+|\-|/|%\*{1,2}|==|>=|==|<=|!=')



# wenn whitespace, nächsten Durchlauf
# Note to myself: z.B. ***, denn * ist gültig und ** ist gültig, *** aber nicht. Wie unterscheiden? Mit Look-Ahead?
# Definition von ++ = #x:x+1. sollte auch gültig sein
