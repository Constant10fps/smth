n = int(input())
animals = []
for i in range(n):
    animals.append(input()[::-1])
animals.sort(reverse=)
animals = [i[::-1] for i in animals]
print(*animals, sep="\n")