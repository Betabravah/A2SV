class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        for i in freq1:
            if i not in freq2:
                return False
        
        
        count1 = Counter(freq1.values())
        count2 = Counter(freq2.values())

        if count1 == count2:
            return True
        
        return False
        
        
        