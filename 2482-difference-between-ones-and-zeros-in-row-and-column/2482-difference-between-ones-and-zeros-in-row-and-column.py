class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        ones_row = defaultdict(int)
        ones_col = defaultdict(int)
        zeroes_row = defaultdict(int)
        zeroes_col = defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1
                    
                else:
                    zeroes_row[i] += 1
                    zeroes_col[j] += 1
                    
        
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = ones_row[i] + ones_col[j] - zeroes_row[i] - zeroes_col[j]
                
        return ans