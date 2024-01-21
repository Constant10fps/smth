n = int(input())
a = list(map(int, input().split(" ")))
s = set()
for i in range(n):
    v = a[i]
    while v in s and v > 0:
        v -= 1
    s.add(v)
print(sum(s))