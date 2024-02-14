t = int(input())
ans = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    idx1 = 0
    count1 = 1
    idx2 = 0
    count2 = 0
    for j in range(1,n):
        if a[j] == a[idx1]:
            count1 += 1
        else:
            idx2 = j
            count2 += 1
    if count1 > 1:
        ans.append(idx2+1)
    if count2 > 1:
        ans.append(idx1+1)
print(*ans, sep = "\n")