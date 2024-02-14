input()
nums = list(map(int, input().split()))
#print(max(max(nums) - 25, 0))
a = [i for i in range(max(nums)) if i not in nums and i <= 25]
print(len(a))