class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        pos = len(candyType) // 2
        
        return pos if len(types) >= pos else len(types)