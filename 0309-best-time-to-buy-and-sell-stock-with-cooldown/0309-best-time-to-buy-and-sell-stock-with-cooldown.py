class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for i_ in range(len(prices) + 2)] # buy, sell
        
        for i in range(len(prices)-1, -1, -1):
            dp[i][0] = max(dp[i+1][1] - prices[i], dp[i+1][0])
            dp[i][1] = max(dp[i+2][0] + prices[i], dp[i+1][1])
            
        return dp[0][0]
         