import sys

nums = [int(sys.stdin.readline()) for _ in range(9)]

max_val = 0
idx = 0

for i in range(len(nums)):
    if max_val < nums[i]:
        max_val = nums[i]
        idx = i + 1


print(max_val)
print(idx)