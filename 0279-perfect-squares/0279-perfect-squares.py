class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x**2 for x in range(n+1) if x**2 <= n]
        nums = [n] * (n+1)
        nums[0] = 0
        
        for i in range(1, n+1):
            for sq in squares:
                if i < sq:
                    break
                    
                if nums[i-sq] < nums[i]:
                    nums[i] = 1 + nums[i-sq]
                    
        return nums[n]
                    

        