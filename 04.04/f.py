n, k = map(int, input().split())
pw = list()
for _ in range(n):
    pw.append(len(input()))
r_pw = len(input())
pw.sort()
c = sum([1 for x in pw if x < r_pw])
r = sum([1 for x in pw if x == r_pw])
t = 0
for i in range(c+1):
    if i % k == 0 and i:
        t += 5
    t += 1
t_min = t
for i in range(c+1, c+r):
    if i % k == 0 and i:
        t += 5
    t += 1
print(t_min, t)