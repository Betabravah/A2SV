class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * (days[-1] + 2)
        dp[days[-1] + 1] = 0
        
        
        for i in days:
            dp[i] = 0
            
        
        for i in range(days[-1], -1, -1):
            if dp[i] == float('inf'):
                dp[i] = dp[i+1]
                
            else:
                
                dp[i] = dp[min(i + 1, days[-1] + 1)] + costs[0]

                dp[i] = min(dp[i], dp[min(i + 7, days[-1] + 1)] + costs[1])

                dp[i] = min(dp[i], dp[min(i + 30, days[-1] + 1)] + costs[2])


        
        return dp[0]
        