from collections import deque
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    s = deque(map(int, input().split()))
    f = deque(map(int, input().split()))
    t = 0
    d_list = []
    while s:
        t0 = max(s.popleft(), t)
        t1 = f.popleft()
        d = t1 - t0
        d_list.append(d)
        t = t1
    ans.append(d_list)
for lists in ans:
    print(*lists)