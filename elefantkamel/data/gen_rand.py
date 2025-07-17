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
d_max = int(cmdlinearg("dmax"))

assert d_max >= 2

n = randint(1, n_max)

ei = []
ki = []

for i in range(n):
    if randint(0, 1):
        ei += [2 * i]
        ki += [2 * i + 1]
    else:
        ei += [2 * i + 1]
        ki += [2 * i]

vals = [randint(1, d_max) for _ in range(2 * n)]
while sum(vals[i] for i in ei) == sum(vals[i] for i in ki):
    vals = [randint(1, d_max) for _ in range(2 * n)]

print(n)
print(*ei)
print(*ki)
print(*vals, sep='\n')