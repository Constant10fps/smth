n = int(input())
row = list(map(int, input().split(" ")))
s = set()
for i in range(n):
    for j in range(i+1, n):
        s.add((row[i], row[j]))
print(len(s))
