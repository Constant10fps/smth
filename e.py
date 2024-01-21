r, c = map(int, input().split(" "))
ber_x = set()
ber_y = set()
for i in range(r):
    s = list(input())
    for j in range(c):
        if s[j] == "S":
            ber_x.add(j)
            ber_y.add(i)
u = set()
for i in range(r):
    for j in range(c):
        if i not in ber_y or j not in ber_x:
            u.add((j, i))
print(len(u))