t = int(input())
a = []
for i in range(t):
    n = int(input())
    sets = list()
    for i in range(3):
        s = set(input().split(" "))
        sets.append(s)
    points = []
    for i in range(3):
        p_p = 0
        for word in sets[i]:
            p = 0
            for j in range(3):
                if i != j and word not in sets[j]:
                    p += 1
            if p == 2:
                p_p += 3
            elif p == 1:
                p_p += 1
        points.append(p_p)
    a.append(points)
for i in a:
    print(*i)