import sys
input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    summ = sum(a)
    if summ > s:
        idx_1 = [i for i in range(n) if a[i]]
        amount = summ - s
        mini = n - idx_1[-amount]
        for left in range(1, amount+1):
            right = amount - left
            if right == 0:
                count = idx_1[left - 1] + 1
            else:
                idx_left = idx_1[left - 1]
                idx_right = idx_1[-right]
                count = (idx_left + 1) + (n - idx_right)
            mini = min(mini, count)
        ans.append(mini)
    elif summ == s:
        ans.append(0)
    else:
        ans.append(-1)
print(*ans, sep="\n")