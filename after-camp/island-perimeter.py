class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        count = 0
        def dfs(row, col, visited):
            nonlocal count

          
            visited[row][col] = True
            
            for row_change, col_change in directions:

                new_row = row + row_change
                new_col = col + col_change
                
                    
                if isbound(new_row, new_col):
                    
                    if grid[row][col] == 1 and grid[new_row][new_col] == 0:
                        count += 1
                    
                    if not visited[new_row][new_col]:
                        dfs(new_row, new_col, visited)
                    
                else:
                    if grid[row][col] == 1:
                        count += 1
        
        
        dfs(0, 0, visited) 
        return count
            