n = int(input())
results = list(map(int, input().split(" ")))
cur = int(input())
a = [i for i in results if i > cur]
print(len(a) + 1)