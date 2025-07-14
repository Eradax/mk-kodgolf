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
nc = n

data = []

while n > 0:
    row = [randint(-1, 0) for _ in range(min(n, 5))]
    data.append(row)
    n -= len(row)

print(nc)
for i in data:
    print(*i)