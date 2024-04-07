n, k = map(int, input().split())
s = input()
start = dict()
finish = dict()
for i, ch in enumerate(s):
    if ch not in start:
        start[ch] = i
    finish[ch] = i
def main():
    open_doors = 0
    for i, ch in enumerate(s):
        if start[ch] == i:
            open_doors += 1
        if open_doors > k:
            return "YES"
        if finish[ch] == i:
            open_doors -= 1
    return "NO"
print(main())