t = int(input())
ans = []
for _ in range(t):
    s = input()
    a = set()
    d = set()
    for i in s:
        if i in a:
            a.remove(i)
            d.add(i)
        else:
            a.add(i)
    s = ""
    for i in a:
        s += i
    for i in d:
        s += i * 2
    ans.append(s)
print(*ans, sep='\n')