tests = int(input())

for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))

    left = right = 0
    total = nums[0]
    positive = True if nums[0] > 0 else False

    while right < len(nums):
        if positive:
            if 0 < nums[left] < nums[right]:
                total += nums[right] - nums[left]
                left = right

            elif nums[right] < 0:
                total += nums[right]
                left = right
                positive = False

        else:
            if nums[left] < nums[right] < 0:
                total += nums[right] - nums[left]
                left = right

            elif nums[right] > 0:
                total += nums[right]
                left = right
                positive = True
        right += 1
    print(total)
