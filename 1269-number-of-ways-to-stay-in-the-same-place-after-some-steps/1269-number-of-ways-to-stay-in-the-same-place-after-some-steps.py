class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dp(idx, step):
            
            if step == 0:
                if idx == 0:
                    return 1
                
                return 0
            
            ans = dp(idx, step-1)
            
            if idx > 0:
                ans += (dp(idx-1, step-1)) % mod
                
            if idx < arrLen - 1:
                ans += (dp(idx+1, step-1)) % mod
                
            return ans
            
        
        mod = 10 ** 9 + 7
        return dp(0, steps) % mod
        