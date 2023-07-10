class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        dp = defaultdict(dict)
        ans = -float('inf')
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                if diff not in dp[j]:
                    dp[j][diff] = 1
                if diff not in dp[i]:
                    dp[i][diff] = 0
                    
                
                dp[i][diff] = dp[j][diff] + 1
                ans = max(ans, dp[i][diff])
                                    
        return ans