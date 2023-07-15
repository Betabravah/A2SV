class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    ignorei = dp[i-1][j]
                    ignorej = dp[i][j-1]
                    
                    dp[i][j] = max(ignorei, ignorej)
                    
                    
        return dp[-1][-1]
                    
        
        
        
        