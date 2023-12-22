class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0] * len(s)
        prefix[0] = 0 if s[0] == '0' else 1
        
        
        for i in range(1, len(s)):
            if s[i] == '1':
                prefix[i] += 1
                
            prefix[i] += prefix[i-1]
            
        
        total = prefix[-1]
        ans = zeroes = 0
        
        for i in range(len(s)-1):
            if s[i] == '0':
                zeroes += 1
                
            ans = max(ans, zeroes + total - prefix[i])
            
        return ans
            
            