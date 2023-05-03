class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(maze), len(maze[0])
        
        
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] != '+'
        
        
        def is_exit(row, col):
            return row == m - 1 or col == n - 1 or row == 0 or col == 0
            
            
        queue = deque([[entrance[0], entrance[1], 0]])
        visited = set((entrance))
        visited.add((entrance[0], entrance[1]))
        
        while queue:
            row, col, steps = queue.popleft()
            
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                    
                    if is_exit(new_row, new_col):
                        return steps + 1
                    
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
                    
                    
        return -1
                    
                    
                    
                    
                    
                    
                    
                    