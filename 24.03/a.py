alphabet = {}
s = input()
for elem in s:
    if elem not in alphabet.keys():
        alphabet[elem] = 1
    else:
        alphabet[elem] += 1
for elem in sorted(alphabet.keys()):
    print(f"{elem} {alphabet[elem]}")