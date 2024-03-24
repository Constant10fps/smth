n = int(input())
d = dict()
ans = []
for _ in range(n):
    s = input()
    if s not in d.keys():
        d[s] = 0
    else:
        d[s] += 1
    ans.append(d[s])
print(*ans, sep="\n")