n = int(input())
acc = 0

while n:
    vals = [int(i) for i in input().split()]
    inds = [i for i, j in enumerate(vals) if j == -1]
    if inds:
        print(*inds)
    else:
        print("Ingen giftig morot")
    acc += len(inds)
    n -= len(vals)
print(acc)