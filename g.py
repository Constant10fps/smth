t = int(input())
a = []
for i in range(t):
    n = int(input())
    s = set(map(int, input().split(" ")))
    if (n - len(s))%2 == 0:
        a.append(len(s))
    else:
        a.append(len(s)-1)
for i in a:
    print(i)