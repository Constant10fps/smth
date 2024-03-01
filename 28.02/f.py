n = int(input())
a = list(map(int, input().split()))
a.sort()
k = 0
prev = 0
for i in range(n):
    if a[i] >= prev+1:
        k += 1
        prev += 1
print(k)