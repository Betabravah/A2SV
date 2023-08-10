class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = Counter(ransomNote)
        freq2 = Counter(magazine)
        
        for i in freq1:

            if freq2[i] < freq1[i]:
                return False
            
        return True