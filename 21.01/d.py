n = int(input())
a = list(map(int, input().split(" ")))
b = [1] * n
right = set()
for i in range(n-1, 1, -1):
    if a[i] in right:
        b[i] = 2
    else:
        right.add(a[i])
ans = len(right)
left = set()
left.add(a[0])
for i in range(1, n-2):
    if b[i] == 1:
        right.remove(a[i])
    elif a[i] not in left:
        left.add(a[i])
        ans += len(right)
print(ans)