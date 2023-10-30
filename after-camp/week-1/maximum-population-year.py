class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        total_years = 2050 - 1950 + 1
        prefix = [0] * total_years
        
        for b, d in logs:
            prefix[b - 1950] += 1
            prefix[d - 1950] -= 1
            
        max_popn = cur_popn = 0
        
        for i in range(total_years):
            cur_popn += prefix[i]
            
            if cur_popn > max_popn:
                max_popn = cur_popn
                ans = i
                
        return ans + 1950