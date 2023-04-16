class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid1), len(grid1[0])
        
        
        def isbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        
        visited = set()
        def dfs(row, col):
            
            visited.add((row, col))
            
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                # connected land is part of island of only grid2
                if isbound(new_row, new_col) and (new_row, new_col) not in visited and grid2[new_row][new_col] == 1:
                    dfs(new_row, new_col)
                    
             
        # visit the islands of only grid2
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j)
                    
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid2[i][j] == 1:
                    islands += 1
                    dfs(i, j)
                    
        return islands
                
                
                