t = int(input())
ans = []
for _ in range(t):
    n, x = map(int, input().split())
    h = sorted(map(int, input().split()))
    row_1, row_2 = h[:n], h[-n:]
    flag = True
    for i in range(n):
        a = row_2[i] - row_1[i]
        if row_2[i] - row_1[i] < x:
            ans.append("NO")
            flag = False
            break
    if flag: ans.append("YES")
print(*ans, sep="\n")