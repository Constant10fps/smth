t = int(input())
a = []
for i in range(t):
    n = int(input())
    s = set(input())
    a.append(n + len(s))
for i in a:
    print(i)