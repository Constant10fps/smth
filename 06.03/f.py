import sys
input = sys.stdin.readline
n = int(input())
ans = []
f = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(n-1):
    x, y = map(int, input().split())
    f[y] = x
    p[x] = y
t = f.index(0, 1)
ans.append(t)
while p[t]:
    ans.append(p[t])
    t = p[t]
print(*ans)