class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)
        mod = ((10) ** 9 + 7)
        dp[0] = 1
        
        for _ in range(n):
            new_dp = [0] * (target + 1)
            for already in range(target+1):
                for event in range(1, k+1):
                    if already - event >= 0:
                        new_dp[already] += dp[already - event]
                        new_dp[already] %= mod
                        
            dp = new_dp
            
        return dp[target] % mod
                    