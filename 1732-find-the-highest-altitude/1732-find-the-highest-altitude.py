class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        ans = 0
        
        for i in gain:
            prefix += i
            ans = max(ans, prefix)
            
        return ans