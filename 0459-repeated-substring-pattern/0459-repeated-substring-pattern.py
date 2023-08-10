class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(len(s)):
            if i != len(s)-1 and len(s[i+1:]) % (i+1) == 0 and s[i+1:] == (s[:i+1] * (len(s[i+1:]) // (i+1))):
                return True
        return False