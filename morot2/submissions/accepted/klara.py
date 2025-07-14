import math
antal=int(input())
antallista=[]

for i in range(math.ceil(antal/5)):
    lista = []
    morotter = list(map(int, input().split()))
    m = 0
    while m < len(morotter):
        if morotter[m] == -1:
            lista.append(m)
            antallista.append(1)
        m += 1
    if lista:
        print(*lista)
    else:
        print("Ingen giftig morot")

print(len(antallista))