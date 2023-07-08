class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        
        for num in arr:
            prev = num - difference
            
            if prev in dp:
                dp[num] = dp[prev]+1
                ans = max(ans, dp[num])
                
            else:
                dp[num] = 1
                
        return ans
            