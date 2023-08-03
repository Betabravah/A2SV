class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ctr = 0
        for i in range(len(s)):
            cur = nums[s[i]]
            
            if i+1 < len(s) and nums[s[i+1]] > cur:
                ctr -= cur
            else:
                ctr += cur
                
        return ctr
                
        
            
                
            
                
            