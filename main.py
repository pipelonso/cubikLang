import sys
from modules.transpile.resolute import Resolute

params = sys.argv

if len(params) > 1:
    if params[2] == 'build':
        Resolute(path=params[1])
