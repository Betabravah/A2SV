class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        
        pairs = sorted(freq.items(), key=lambda x: x[1])
               
        uniques = len(freq)
        
        for i, j in pairs:
            if k <= 0:
                break
            
            k -= j
            
            if k >= 0:
                
                uniques -= 1
                
        return uniques
            
        
        