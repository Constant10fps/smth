t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    b = input().split(" ")
    a = ["0"] * n
    idx_s = 0
    idx_e = n - 1
    i = 0
    while idx_s <= idx_e:
        if not i%2:
            a[i] = b[idx_s]
            idx_s += 1
        else:
            a[i] = b[idx_e]
            idx_e -= 1
        i += 1
    ans.append(" ".join(a))
print(*ans, sep="\n")