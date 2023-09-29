class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        
        @cache
        def backtrack(idx):
            if idx == len(s):
                return True
            
            for i in range(idx, len(s)):
                cur = s[idx: i+1]
                
                if cur in word_dict and backtrack(i+1):
                    return True
                
        return backtrack(0)
            
            
            
            
        