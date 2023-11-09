class Solution:
    def countHomogenous(self, s: str) -> int:
        left = ans = 0 
        
        for right in range(len(s)):
            if s[right] != s[left]:

                n = right - left
                ans += (n * (n+1) // 2)
                
                left = right
            
        n = right - left + 1
        ans += (n * (n+1) // 2)
            
        return int(ans) % (10 ** 9 + 7)