import sys
from collections import deque
input = sys.stdin.readline
q1 = deque()
q2 = deque()
n = int(input())
ans = []
for i in range(n):
    cur = input()
    if cur[0] == "+":
        q2.append(int(cur[1:]))
    elif cur[0] == "-":
        ans.append(q1.popleft())
    else:
        q2.appendleft(int(cur[1:]))
    if len(q2) > len(q1):
        q1.append(q2.popleft())
print(*ans, sep="\n")