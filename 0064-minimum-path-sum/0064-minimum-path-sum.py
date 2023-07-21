class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def get_parents(row, col):
            parents = []
            
            if row - 1 >= 0:
                parents.append((row - 1, col))
            if col - 1 >= 0:
                parents.append((row, col - 1))
                
            return parents
        
        
        
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        
        
        for i in range(rows):
            for j in range(cols):
                parents = get_parents(i, j)
                
                temp = float('inf')
                for par in parents:
                    temp = min(temp, dp[par[0]][par[1]])
                    
                temp = 0 if temp == float('inf') else temp
                    
                dp[i][j] = grid[i][j] + temp
                
                
        return dp[-1][-1]
                
                