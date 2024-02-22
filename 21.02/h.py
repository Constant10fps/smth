t = int(input())
ans = []
for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    cur = a[0]
    c = 1
    flag = True
    for i in range(1,n):
        if a[i] != cur:
            c = 1
            cur = a[i]
        else: c += 1
        if c == 3:
            ans.append(cur)
            flag = False
            break
    if flag:
        ans.append("-1")
print(*ans, sep="\n")