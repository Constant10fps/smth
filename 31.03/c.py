n, k = map(int, input().split())
s = input()
start = dict()
finish = dict()
for i, ch in enumerate(s):
    if ch not in start:
        start[ch] = i
        finish[ch] = i
    else:
        finish[ch] = i
d = dict()
for value in start.values():
    d[value] = 1
for value in finish.values():
    d[value] = -1
summ = 0
max_i = 0
for key in sorted(d):
    summ += d[key]
    max_i = max(max_i, summ)
if max_i <= k:
    print("NO")
else:
    print("YES")