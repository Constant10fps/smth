n = int(input())
d = dict()
s = input()
for i in range(n-1):
    sl = s[i:i+2]
    if sl not in d:
        d[sl] = 1
    else:
        d[sl] += 1
print(max(d, key=d.get))
