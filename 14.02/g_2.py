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
            summ += sum(abl_fire) * 2
            count_2 = len(abl_fire)
            count_1 = len(abl_frost) - count_2
            summ += sum(abl_frost[-count_2:]) * 2 + sum(abl_frost[:count_1])
        elif len(abl_fire) > len(abl_frost):
            summ += sum(abl_frost) * 2
            count_2 = len(abl_frost)
            count_1 = len(abl_fire) - count_2
            summ += sum(abl_fire[-count_2:]) * 2 + sum(abl_fire[:count_1])
        else:
            summ = sum(damage) * 2 - min(damage)
        ans.append(summ)
    elif abl_frost:
        ans.append(sum(abl_frost))
    elif abl_fire:
        ans.append(sum(abl_fire))
print(*ans, sep='\n')
