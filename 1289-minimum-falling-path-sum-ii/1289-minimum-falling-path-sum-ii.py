class Solution:
    def minFallingPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        dp = [[0] * m for _ in range(2)]
        
        for j in range(m):
            dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(m):
                dp[i % 2][j] = grid[i][j]
                
                minPrev = float('inf')
                for k in range(m):
                    if k != j:
                        minPrev = min(minPrev, dp[(i - 1) % 2][k])
                dp[i % 2][j] += minPrev
        
        minSum = float('inf')
        for j in range(m):
            minSum = min(minSum, dp[(n - 1) % 2][j])
        
        return minSum