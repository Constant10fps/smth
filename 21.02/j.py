t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    s = input()
    ss = sorted(s)
    c = n
    for i in range(n):
        if s[i] == ss[i]:
            c -= 1
    ans.append(c)
print(*ans, sep="\n")