class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        for right in range(k):
            maxSum += nums[right]

        left = 0
        sum = maxSum
        while right + 1  < len(nums):
            sum -= nums[left]
            sum += nums[right + 1]
            left += 1
            right += 1

            maxSum = max(maxSum, sum)
        return maxSum / k

        