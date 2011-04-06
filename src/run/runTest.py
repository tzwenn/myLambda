#!/usr/bin/env python

import sys

if '..' not in sys.path:
	sys.path.append('..')

import evaluate
from symbols import *

env = evaluate.Environment()
# eins = 1.
_1 = Value(1)
bindRes = env(Bind('eins', _1))
_eins = Name('eins')
_rek_call = Call(Name('*'), [Name('n'), Call(Name('fac'), [Call(Name('-'), [Name('n'), Value(1)])])])
_fak = Func(['n'], Call(Name('if'), [Call(Name('=='), [Name('n'), Value(0)]), Value(1), _rek_call]))
env(Bind('fac', _fak))

print env(Call(Name('fac'), [Value(5)])).value
