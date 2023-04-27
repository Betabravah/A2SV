class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1
        
        
        
        rotten = deque()
        visited = set()
        fresh_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    rotten.append([i, j])
                    visited.add((i, j))
                
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        
        minutes = 0
        
        while rotten:
            
            minutes += 1
            length = len(rotten)
            
            for i in range(length):
                curi, curj = rotten.popleft()
                
                
                for row_change, col_change in directions:
                    
                    new_row = curi + row_change
                    new_col = curj + col_change
                    
                    if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                        fresh_count -= 1
                        rotten.append((new_row, new_col))
                        visited.add((new_row, new_col))
        
        if fresh_count == 0:
            return minutes - 1
        
        return -1
            