def function(d: dict):
    if len(d) == 1:
        return "Yes"
    if d[max(d, key=d.get)] < 2:
        return "No"
    return "Yes"
n = int(input())
d = dict()
s = input()
for elem in s:
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] += 1
print(function(d))