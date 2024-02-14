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
            for i in range(twos):
                if i%2 == 0:
                    summ += 2 * abl_frost[-1]
                    abl_frost.pop(-1)
                else:
                    summ += 2 * abl_fire[-1]
                    abl_fire.pop(-1)
            summ += sum(abl_frost)
        elif len(abl_fire) > len(abl_frost):
            twos = len(abl_frost) + 1
            for i in range(twos):
                if i % 2 == 0:
                    summ += 2 * abl_fire[-1]
                    abl_fire.pop(-1)
                else:
                    summ += 2 * abl_frost[-1]
                    abl_frost.pop(-1)
            summ += sum(abl_fire)
        else:
            summ = sum(damage) * 2 - min(damage)
        ans.append(summ)
    elif abl_frost:
        ans.append(sum(abl_frost))
    elif abl_fire:
        ans.append(sum(abl_fire))
print(*ans, sep='\n')
