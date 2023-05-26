class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        
        def climb(n):
            nonlocal memo
            
            if n < 2:
                return 0
            
            
            if n not in memo:
                memo[n] = min(climb(n - 1) + cost[n - 1], climb(n - 2) + cost[n - 2])
                
            return memo[n]
        
        
        return climb(len(cost))
        
        