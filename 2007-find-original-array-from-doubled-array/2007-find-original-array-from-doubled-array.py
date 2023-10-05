class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = Counter(changed)
        
        ans = []
        
        changed.sort()
        
        for i in changed:
            if freq[i] > 0:
                freq[i] -= 1
                
                if freq[i*2] > 0:
                    freq[i*2] -= 1
                
                    ans.append(i)
                
        if len(ans) == len(changed) / 2:
            return ans
        
        return []
        
                