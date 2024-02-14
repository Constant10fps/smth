t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    i_s = 1
    i_e = -1
    sum_r = 0
    sum_s = s[i_s]
    while sum_r <= sum_s and i_s - i_e <= n:
        sum_r += s[i_e]
        i_e -= 1
        sum_s += s[i_s]
        i_s += 1
    if sum_r > sum_s:
        ans.append("YES")
    else:
        ans.append("NO")
print(*ans, sep="\n")