class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            nonlocal area
            nonlocal max_area
            
            visited.add((row, col))
            
            area += 1
            max_area = max(max_area, area)
                            
            
            for row_change, col_change in directions:
                new_row, new_col = row + row_change, col + col_change
                
                
                if isbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col]:
                    dfs(new_row, new_col)
                    
                    
        visited = set()
        max_area = area = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j]:
                    area = 0
                    dfs(i, j)
            
        return max_area