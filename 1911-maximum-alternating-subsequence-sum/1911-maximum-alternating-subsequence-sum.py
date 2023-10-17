class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(2)] 
        
        for i in range(n):
            dp[0][i] = max(dp[1][i-1] - nums[i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1] + nums[i], dp[1][i-1])
            
        return max(dp[-1])