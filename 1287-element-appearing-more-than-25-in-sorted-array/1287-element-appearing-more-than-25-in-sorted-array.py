class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        
        for i, c in count.items():
            if c > n // 4:
                return i
            
            