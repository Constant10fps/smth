n = int(input())
a = set()
b = set()
for i in range(n):
    x, y = map(int, input().split(" "))
    if x != 0 and (y, -x) in a:
        if (y, -x) not in b:
            b.add((y,x))
        a.remove((y,-x))
    else:
        a.add((y,x))
b = list(b)
b.sort()
print(len(b))
for elem in b:
    print(f"({-abs(elem[1])}, {elem[0]}) - ({abs(elem[1])}, {elem[0]})")
