n = int(input())
e = [int(i) for i in input().split()]
k = [int(i) for i in input().split()]

vals = [int(input()) for _ in range(2 * n)]

ev = [vals[i] for i in e]
kv = [vals[i] for i in k]

et = sum(ev)
kt = sum(kv)

d = abs(et - kt)
s = d % 60
d //= 60
m = d % 60
d //= 60
h = d

time = f"{h:0>2}:{m:0>2}:{s:0>2}"

print("Elefant" if et < kt else "Kamel")
print(time)