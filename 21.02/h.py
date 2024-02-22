t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s_a = set(a)
    cur = []
    for e in s_a:
        if a.count(e) >= 3:
            cur.append(e)
    ans.append(cur[0] if cur else "-1")
print(*ans, sep="\n")