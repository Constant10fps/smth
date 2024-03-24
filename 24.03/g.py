sm = 0
n = int(input())
balls = map(int, input().split())
d = dict()
for elem in balls:
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] += 1
for i in sorted(d.keys()):
    k1 = d[i]
    k2 = d.get(i * 2, 0)
    k3 = d.get(i * 4, 0)
    k = min(k1, k2, k3)
    sm += k
    if k > 0:
        d[i] -= k
        d[i * 2] -= k
        d[i * 4] -= k
print(sm)