class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, minn = 0, prices[0]
        
        for num in prices:
            if num < minn:
                minn = num
            ans = max(ans, num - minn)
            
        return ans