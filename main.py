n, m = map(int, input().split(" "))
a = set()
for i in range(n):
    s = input().split()
    x = int(s[0])
    for j in range(x):
        y = int(s[j+1])
        a.add(y)
if len(a) == m:
    print("YES")
else:
    print("NO")