n = int(input())
a = list(map(int, input().split()))
st = []
ans = [-1] * n
for i in range(len(a)):
    while st and st[-1][0] > a[i]:
        ans[st[-1][1]] = i
        st.pop()
    st.append((a[i], i))
print(*ans)