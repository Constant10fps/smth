n = int(input())
d = dict()
hor = dict()
ver = dict()
time = 0
for _ in range(n):
    s = input().split()
    command = s[0]
    pos = int(s[1])
    color = int(s[2])
    time += 1
    if command == "h":
        hor[pos] = (color, time)
    if command == "v":
        ver[pos] = (color, time)
    if command == "?":
        x, y = pos, color
        ch, th = hor.get(x, (0, 0))
        cv, tv = ver.get(y, (0, 0))
        if th > tv:
            print(ch)
        else:
            print(cv)