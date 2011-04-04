import sys

if '..' not in sys.path:
	sys.path.append('..')

import evaluate
from symbols import *

env = evaluate.Environment()
_1 = Value(1)
bindRes = env.evaluate(Bind('eins', _1))
_eins = Name('eins')
