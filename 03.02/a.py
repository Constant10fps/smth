n = int(input())
nums = list(map(int, input().split()))
s = 0
d = 0
for i in range(n//2):
    if nums[0] > nums[-1]:
        s += nums[0]
        nums.pop(0)
    else:
        s += nums[-1]
        nums.pop(-1)
    if nums[0] > nums[-1]:
        d += nums[0]
        nums.pop(0)
    else:
        d += nums[-1]
        nums.pop(-1)
if nums:
    s += nums[0]
print(s, d)