class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1: return 1

        return ((2 * n - 1) * self.countOrders(n-1) * n) % (10**9 + 7)
        
