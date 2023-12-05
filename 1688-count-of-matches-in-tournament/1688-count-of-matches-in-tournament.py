class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        
        while n > 1:
            if n % 2:
                passed = (n-1) / 2
                ans += passed + 1
            else:
                ans += (n // 2)
                
            
            n //= 2
            
        return int(ans)