arr = sorted(set(map(int, input().split(","))))
start = arr[0]
prev = start
ans = []
for cur_page in arr:
    if cur_page > prev + 1:
        if prev == start:
            ans.append(str(start))
        else:
            ans.append(f"{start}-{prev}")
        start = cur_page
        prev = start
    else:
        prev = cur_page
if prev == start:
    ans.append(str(start))
else:
    ans.append(f"{start}-{prev}")
print(*ans, sep=",")