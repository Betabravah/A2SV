class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        indices = [(sr, sc)]
        visited = set()
        start = image[sr][sc]
        
        def dfs(row, col):
            
            visited.add((row, col))
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if isbound(new_row, new_col) and image[new_row][new_col] == start and (new_row, new_col) not in visited:
                    
                    indices.append((new_row, new_col))
                    dfs(new_row, new_col)
          
        dfs(sr, sc) 
        for r, c in indices:
            image[r][c] = color
         

        return image
            
            
            