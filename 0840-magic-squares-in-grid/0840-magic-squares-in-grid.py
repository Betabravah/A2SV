class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        count = 0
        
        for r in range(len(grid) - 2):
            for c in range(len(grid) - 2):
                temp_grid = [grid[r+k][c:c+3] for k in range(3)]
                
                if self.isMagicSquare(temp_grid):
                    count += 1
                    
        return count
    
    def isMagicSquare(self, grid):
        flat = []
        for row in grid:
            for col in row:
                flat.append(col)
        
        if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        
        
        row_sum = [sum(row) for row in grid]
        col_sum = [sum([row[i] for row in grid]) for i in range(3)]
        diag_sum = [sum([grid[i][i] for i in range(3)]), (grid[0][2] + grid[1][1] + grid[2][0])]
        row_sum.extend(col_sum)
        row_sum.extend(diag_sum)
        
        return len(set(row_sum)) == 1
        