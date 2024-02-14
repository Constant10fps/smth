t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    abilities = list(map(int, input().split()))
    damage = list(map(int, input().split()))
    abl_fire = []
    abl_frost = []
    for i in range(n):
        if abilities[i]:
            abl_frost.append(damage[i])
        else:
            abl_fire.append(damage[i])
    abl_fire.sort()
    abl_frost.sort()
    summ = 0
    if abl_frost and abl_fire:
        if len(abl_frost) > len(abl_fire):
            twos = len(abl_fire) + 1
    elif abl_frost:
        ans.append(sum(abl_frost))
    elif abl_fire:
        ans.append(sum(abl_fire))
print(*ans, sep='\n')
