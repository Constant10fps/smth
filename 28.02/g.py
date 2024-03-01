t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    t = a[0]
    b = [elem for elem in a if elem > t]
    b.sort()
    for elem in b:
        diff = elem - t
        t += diff//2 + diff%2
    ans.append(t)
print(*ans, sep="\n")