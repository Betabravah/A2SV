class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sums = 0
        minLen = len(nums)
        if sum(nums) < target:
            return 0
        else:
            for right in range(len(nums)):
                sums += nums[right]
                while sums >= target:
                    minLen = min(minLen, right - left + 1)
                    sums -= nums[left]
                    left += 1
            
            return minLen
