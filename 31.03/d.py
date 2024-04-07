t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for elem in a:
        d[elem] = d.get(elem, 0) + 1
        d[elem + 1] = d.get(elem+1, 0)
    sd = sorted(d)
    ans = d[sd[0]]
    y = d[sd[0]]
    for i in range(1, len(sd)):
        cur = sd[i]
        x = d[cur]
        if x > y:
            ans += (x - y)
        y = x
    print(ans)