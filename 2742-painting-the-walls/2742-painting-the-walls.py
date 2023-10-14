class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache
        def dp(i, remain):
            if remain <= 0:
                return 0
            
            if i == len(cost):
                return inf
            
            paint = dp(i+1, remain -1 - time[i]) + cost[i]
            
            dont_paint = dp(i+1, remain)
            
            return min(paint, dont_paint)
        
        return dp(0, len(cost))