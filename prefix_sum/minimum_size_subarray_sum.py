class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = prefix = 0
        minLength = len(nums)
        totalSum = sum(nums)
        
        if totalSum < target:
            return 0
        
        for end in range(len(nums)):
            prefix += nums[end]
            while prefix >= target:
                minLength = min(minLength, end - start + 1)
                prefix -= nums[start]
                start += 1

        return minLength
