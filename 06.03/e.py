import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
ans = []
n = int(input())
add = 0
for i in range(n):
    event = list(map(int, input().split()))
    if event[0] == 1:
        queue.append([event[1], add])
    elif event[0] == 2:
        queue[0][0] += event[1] - event[2]
        add += event[2]
    else:
        exit = queue.popleft()
        ans.append(exit[0] + add - exit[1])
print(*ans, sep="\n")