n = int(input())
a = set()
b = set()
for i in range(n):
    x, y = map(int, input().split(" "))
    if x != 0 and (y, -x) in a:
        b.add((y,-abs(x)))
    else:
        a.add((y,x))
b = list(b)
b.sort()
print(len(b))
for elem in b:
    print(f"({elem[1]}, {elem[0]}) - ({-elem[1]}, {elem[0]})")
