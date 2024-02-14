n, t = map(int, input().split())
days = list(map(int, input().split()))
time = [86400 - i for i in days]
sums = [sum(time[0:i]) for i in range(n)]
sums_min = [i for i in sums if i < t]
print(len(sums_min))