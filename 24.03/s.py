import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    small = []
    big = []
    s = list(input())
    for i in range(len(s)-1):
        if s[i].isupper() and s[i] != "B":
            big.append(i)
        elif s[i].islower() and s[i] != "b":
            small.append(i)
        elif s[i] == "B" and big:
            s[big.pop()] = "*"
        elif s[i] == "b" and small:
            s[small.pop()] = "*"
    for elem in s:
        if elem not in "bB*":
            print(elem, end="")