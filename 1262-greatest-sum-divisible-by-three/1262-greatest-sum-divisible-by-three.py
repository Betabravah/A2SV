class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0] 
    
        for num in nums:
            for i in dp[:]:
                temp = num + i
                dp[temp % 3] = max(dp[temp % 3], temp)
                
        return dp[0]