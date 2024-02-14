r, c = map(int, input().split(" "))
a = []
for i in range(r):
    a.append(input())
for i in range(1, r+1):
    s = set()
    for j in range(c):
        b = str()
        for k in range(r-i, r):
            b += a[k][j]
        s.add(b)
    if len(s) == c:
        print(r-i)
        break
