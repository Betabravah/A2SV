class Solution:
    def minimizedStringLength(self, s: str) -> int:
        freq = Counter(s)
        
        return len(freq.values())