t = int(input())
ans = []
for i in range(t):
    n= int(input())
    meow = input().upper()
    a = [meow[0]]
    for let in meow:
        if a[-1] != let:
            a.append(let)
    if "".join(a) == "MEOW":
        ans.append("YES")
    else:
        ans.append("NO")
print(*ans, sep="\n")