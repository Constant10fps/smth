n = int(input())
h = list(map(int, input().split()))
h_d = [h[i+1] - h[i] if h[i+1] > h[i] else 0 for i in range(n-1)]
k = int(input())
min_d = sum(h_d[0:k-1])
min_s = 1
d = min_d
for i in range(1, n-k+1):
    d = d - h_d[i-1] + h_d[i+k-2]
    if d < min_d:
        min_d = d
        min_s = i+1
print(min_s)
print(min_d)