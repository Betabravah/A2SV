class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        
        if grid[0][0] == 1:
            return -1
        
        
        
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        
        visited = set([(0, 0)])
        queue = deque([(0, 0, 1)])        
        
        while queue:
            cur_row, cur_col, length = queue.popleft()
            
            if (cur_row, cur_col) == (n - 1, n - 1):
                        return length
            
            for row_change, col_change in directions:
                
                new_row = cur_row + row_change
                new_col = cur_col + col_change
                
                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                
                    
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, length + 1))
                    
                    
        return -1
                
                
                
                
                
                
                
                
                