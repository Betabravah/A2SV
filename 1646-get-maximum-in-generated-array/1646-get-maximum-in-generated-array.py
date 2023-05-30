class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        
        if n == 0:
            return 0
        
        def dp(n):
            nonlocal memo
            if n <= 1:
                return n
            
            if n not in memo:
                if n % 2 == 1:
                    memo[n] = dp(n // 2) + dp(ceil(n / 2))
                    
                else:
                    memo[n] = dp(n // 2)
                    
            return memo[n]

        ans = -inf
        for i in range(n+1):
            dp(i)
            ans = max(ans, memo[i])
            
        
        return ans