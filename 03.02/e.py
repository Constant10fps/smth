n = int(input())
piles = list(map(int, input().split()))
m = int(input())
worms = list(map(int, input().split()))
k = sum(piles)
r = [0] * k
x = 1
pos = 0
for s in piles:
    for _ in range(s):
        r[pos] = x
        pos +=1
    x += 1
for _ in range(m):
    t = worms[_]
    print(r[t-1])