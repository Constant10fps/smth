votes = int(input())
count = dict()
for _ in range(votes):
    vote = input()
    if vote not in count:
        count[vote] = 1
    else:
        count[vote] += 1
vote_max = count[max(count, key=count.get)]
winners = sorted([elem for elem in count if count[elem] == vote_max])
print(*winners, sep="\n")
