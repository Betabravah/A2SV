class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        
        seen = [False] * (len(arr) + 1)
        
        for i in freq:
            count = freq[i]
            if seen[count]:
                return False
            
            seen[count] = True
            
        return True