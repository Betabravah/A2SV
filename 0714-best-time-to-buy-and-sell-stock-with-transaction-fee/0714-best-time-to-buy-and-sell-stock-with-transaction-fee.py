class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        
        def dp(n, hold):
            if n == len(prices):
                return 0
            
            state = (n, hold)
            
            if state not in memo:
                memo[state] = dp(n+1, hold)
                
                if hold:
                    memo[state] = max(memo[state], dp(n+1, False) - prices[n])
                else:
                    memo[state] = max(memo[state], dp(n+1, True) + prices[n] - fee)
                    
                    
            return memo[state]
        
        
        return dp(0, True)