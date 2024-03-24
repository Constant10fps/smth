import sys
input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    small = []
    big = []
    s = list(input()[:-1])
    for i in range(len(s)):
        if s[i].isupper() and s[i] != "B":
            big.append(i)
        elif s[i].islower() and s[i] != "b":
            small.append(i)
        elif s[i] == "B" and big:
            s[big.pop()] = "*"
        elif s[i] == "b" and small:
            s[small.pop()] = "*"
    ans_s = str()
    for elem in s:
        if elem not in "bB*":
            ans_s += elem
    ans.append(ans_s)
print(*ans, sep="\n")