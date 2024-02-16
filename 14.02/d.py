n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    if not a or a[-1] != (x,y):
        a.append((x,y))
lines = set()
duplicates = set()
for i in range(1,len(a)):
    if (a[i-1], a[i]) in lines or (a[i], a[i-1]) in lines:
        if ((a[i-1], a[i]) not in duplicates 
        and (a[i], a[i-1]) not in duplicates):
            duplicates.add((a[i-1], a[i]))
    lines.add((a[i-1], a[i]))
print(len(duplicates))