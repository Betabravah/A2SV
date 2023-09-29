class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict = set(wordDict)
        
        def backtrack(index, words):
            nonlocal ans
            
            if index == len(s):
                ans.append(' '.join(words))
                return
            
            for i in range(index, len(s)):
                cur = s[index:i+1]
                
                if cur in word_dict:
                    backtrack(i+1, words + [cur])
                    
        ans  = []
        backtrack(0, [])
        return ans
                
                
                
                
                
            
        