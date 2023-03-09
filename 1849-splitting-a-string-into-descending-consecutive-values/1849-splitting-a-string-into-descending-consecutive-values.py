class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(prev, idx):
            if idx >= len(s):
                return True
            
            res = False
            for i in range(idx, len(s)):
                if prev -1 == int(s[idx:i+1]):
                    res = res or backtrack(int(s[idx:i+1]), i+1)
            
            return res
        
        res = False
        for i in range(len(s)-1):
            res = res or backtrack(int(s[:i+1]), i+1)
        return res
            