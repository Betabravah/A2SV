class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        
        ans = 0
        got_odd = False
        
        for i in freq:
            
            if freq[i] % 2:
                got_odd = True
                ans += (freq[i] - 1)
                    
            else:
                ans += freq[i]
                
        return ans + 1 if got_odd else ans