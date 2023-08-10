class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        
        for idx, char in enumerate(s):
            if freq[char] == 1:
                return idx
        return -1