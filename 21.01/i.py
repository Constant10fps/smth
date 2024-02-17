r, c = map(int, input().split(" "))
columns = [""] * c
for i in range(r):
    s = input()
    for j in range(len(s)):
        columns[j] = s[j] + columns[j]
b = set(columns)
ans = 0
while len(b) == c:
    d = set()
    for s in b:
        d.add(s[:-1])
    ans += 1
    b = d
print(ans-1)