class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        left, right = 0, n-1
        
        while left < right:
            
            if s[left] != s[right]:
                break
                
            while left + 1 < right and s[left] == s[left + 1]:
                left += 1
                
            while right - 1 > left and s[right] == s[right - 1]:
                right -= 1
                
            left += 1
            right -= 1
            
                
                
        return right - left + 1