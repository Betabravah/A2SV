class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxCoins = 0
        for i in range(len(piles)-2, len(piles)//3-1, -2):
            maxCoins += piles[i]
        
        return maxCoins