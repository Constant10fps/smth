n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sam = [-1] * n
cheat = [-1] * n
for mark in range(5, 1, -1):
    for i in range(n):
        if a[i] == mark:
            adj = []
            if i > 0 and sam[i-1] > mark:
                adj.append(sam[i-1])
            if i+1 < n and sam[i+1] > mark:
                adj.append(sam[i+1])
            if adj:
                cheat[i] = max(adj)
            else:
                sam[i] = mark
new = [max(sam[i], cheat[i]) for i in range(n)]
print(*new, sep="\n")