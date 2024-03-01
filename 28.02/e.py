n = int(input())
d = [0]
st = []
ans = []
for i in range(n):
    a = input()
    if a[0] == "+":
        st.append(a[1:])
        d.append(d[-1] + int(a[1:]))
    elif a[0] == "?":
        ans.append(d[-1] - d[-int(a[1:])-1])
    else:
        ans.append(st[-1])
        d.pop()
        st.pop()
print(*ans, sep="\n")