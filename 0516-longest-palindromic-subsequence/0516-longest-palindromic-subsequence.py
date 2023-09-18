class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        reversed = s[::-1]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(dp[i])):
                if s[i-1] == reversed[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    ignorei = dp[i-1][j]
                    ignorej = dp[i][j-1]
                    
                    dp[i][j] = max(ignorei, ignorej)
        
        return dp[-1][-1]