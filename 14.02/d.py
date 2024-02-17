def ts(a, b):
    return (a,b) if a < b else (b,a)
n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    if not a or a[-1] != (x,y):
        a.append((x,y))
lines = set()
duplicates = set()
for i in range(1,len(a)):
    if ts(a[i-1], a[i]) in lines:
        duplicates.add(ts(a[i-1], a[i]))
    else:
        lines.add(ts(a[i-1], a[i]))
print(len(duplicates))