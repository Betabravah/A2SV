class Solution:
    def longestPrefix(self, s: str) -> str:
        
        lps = [0] * len(s)
        prevLps, i = 0, 1
        ans = 0
        
        while i < len(s):
            
            if s[i] == s[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
                
                ans = max(ans, prevLps)
                
            else:
                if prevLps == 0:
                    i += 1
                    
                else:
                    prevLps = lps[prevLps - 1]
                          
        return s[:lps[-1]]
                    
        