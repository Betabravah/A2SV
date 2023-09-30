class Solution:
    def canReach(self, s: str, mn: int, mx: int) -> bool:
        n = len(s)
        
        dp = [False] * n
        dp[0] = True
        
        a = 0
        for i in range(n):
            if not dp[i]:
                continue

            b = min(i + mx, n - 1)

            for j in range(max(a, i + mn), b + 1):
                if s[j] == '0':
                    dp[j] = True
                    
            a = b + 1

        return dp[n - 1]