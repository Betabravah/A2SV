n = int(input())
nums = list(map(int, input().split()))

even = odd = False
for num in nums:
    if num % 2:
        odd = True
    else:
        even = True

    if odd and even:
        nums.sort()
        break

print(*nums)
