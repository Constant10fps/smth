import sys
input = sys.stdin.readline
nums = list(map(int, input().split(" ")))
min_idc = [i for i in range(5) if nums[i] == min(nums)]
max_idc = [i for i in range(5) if nums[i] == max(nums)]
for i in range(5):
    if i == min_idc[0] or i == max_idc[-1]:
        print(f"({nums[i]})", end = " ")
    else:
        print(nums[i], end = " ")
print(f"= {sum(nums) - max(nums) - min(nums)}")