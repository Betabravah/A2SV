class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        k = ans = 0
        
        for i in range(len(flips)):
            k = max(k, flips[i])
            
            if k == i+1:
                ans += 1
                
        return ans