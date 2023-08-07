class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        path = {
            1: [(0, -1), (0, 1)] ,
            2: [(-1, 0), (1, 0)] ,
            3: [(0, -1), (1, 0)] ,
            4: [(0, 1), (1, 0)] ,
            5: [(0, -1), (-1, 0)] ,
            6: [(0, 1), (-1, 0)] ,
        }
        
        def is_bound(row, col):
            return 0 <= row < rows and 0 <= col < cols and (row, col) not in visited
        
        queue = deque([(grid[0][0], 0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            street, row, col = queue.popleft()
            
            if (row, col) == (rows - 1, cols - 1):
                return True
            
            for row_change, col_change in path[street]:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_bound(new_row, new_col) and (-row_change, -col_change) in path[grid[new_row][new_col]]:
                    queue.append((grid[new_row][new_col], new_row, new_col))
                    visited.add((new_row, new_col))
                    
        return False