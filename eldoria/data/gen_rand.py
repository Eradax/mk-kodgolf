#!/usr/bin/env python3

import sys
import random
from random import randint

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    if default is None:
        print("missing parameter", name)
        sys.exit(1)
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

n_max = int(cmdlinearg("nmax"))
n = randint(1, n_max)

edg = [randint(1, i+1) for i in range(1, n)]

print(n)
for i in edg:
    print(i)