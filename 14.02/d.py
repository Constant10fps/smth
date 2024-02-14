n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x,y))
lines = set()
duplicates = set()
for i in range(1,n):
    if (a[i-1], a[i]) in lines or (a[i], a[i-1]) in lines:
        if ((a[i-1], a[i]) not in duplicates 
        or  (a[i], a[i-1]) not in duplicates):
            duplicates.add((a[i-1], a[i]))
    else:
        lines.add((a[i-1], a[i]))
print(len(duplicates))