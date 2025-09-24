#!/usr/bin/env python3

n = int(input())
assert(n <= 5000)

e = [-1] * (n + 1)
def find(x):
    if e[x] < 0:
        return x
    else:
        e[x] = find(e[x])
        return e[x]
    
def join(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return 0
    
    if e[a] > e[b]:
        a, b = b, a

    e[a] += e[b]
    e[b] = a

for i in range(1, n):
    u = int(input())
    v = i + 1
    join(u, v)

print(-min(e))