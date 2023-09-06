class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        
        for idx, i in enumerate(s):
            if words[idx][0] != i:
                return False
            
        return True
            