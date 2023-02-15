tests = int(input())

for test in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    right = 1
    ctr = 0
    while right < n:
        if abs(nums[right-1] - nums[right]) == 1:
            ctr += 1
        elif nums[right-1] == nums[right]:
            ctr += 1
        right += 1
    if n > 1 and ctr == n - 1:
        print("YES")
    elif n == 1:
        print("YES")
    else:
        print("NO")
