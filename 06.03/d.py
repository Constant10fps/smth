from collections import deque
p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))
c = 0
while c <= 1000000:
    c += 1
    if p1[0] == 0 and p2[0] == 9:
        p1.append(p1.popleft())
        p1.append(p2.popleft())
    elif p2[0] == 0 and p1[0] == 9:
        p2.append(p1.popleft())
        p2.append(p2.popleft())
    elif p1[0] > p2[0]:
        p1.append(p1.popleft())
        p1.append(p2.popleft())
    elif p2[0] > p1[0]:
        p2.append(p1.popleft())
        p2.append(p2.popleft())
    if not p1:
        print(f"second {c}")
        break
    elif not p2:
        print(f"first {c}")
        break
else:
    print("botva")