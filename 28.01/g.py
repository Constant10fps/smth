n = int(input())
a = []
for i in range(n):
    room = list(map(int, input().split(" ")))
    a.append(room[1] - room[0])
print(len([i for i in a if i >= 2]))