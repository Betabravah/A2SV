class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in piles:
            heappush(heap, -i)
        
        while k:
            pile = heappop(heap)
            pile //= 2
            heappush(heap, pile)
            k -= 1
            
        return -sum(heap)