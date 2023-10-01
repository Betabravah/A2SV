class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [i for i in nums]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i] + dp[i-1])
            
        return max(dp)