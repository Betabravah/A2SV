class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col, visited):
            
            if (row, col) in visited:
                return
            
             
            visited.add((row, col))
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if isbound(new_row, new_col) and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col, visited)
                
                
        count = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i, j, visited)
                    
                    
        return count
        
            
           
                