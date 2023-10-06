class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        
        @cache
        def dp(num):
            nonlocal ans
            
            for i in range(1, num):
                one = dp(i)
                two = dp(num - i)
                
                ans = max(ans, one * two, i * (num-i), one * (num-i), i * two)
                
            return ans
        
        return dp(n)