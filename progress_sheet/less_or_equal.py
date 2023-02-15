n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()

if k == 0 and nums[0] > 1:
    print(nums[0] - 1)
elif k < n and nums[k - 1] < nums[k]:
    print(nums[k - 1])
elif k == n:
    print(nums[-1])
else:
    print(-1)
