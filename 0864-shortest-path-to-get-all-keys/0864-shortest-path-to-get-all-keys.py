class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        queue = deque()
        keys = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    queue.append((i, j, tuple(), 0))
                    
                elif grid[i][j].islower():
                    keys += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#'
        
        visited = set()
        
        while queue:
            row, col, cur_keys, moves = queue.popleft()
            
            if (row, col, cur_keys) not in visited:
                
                visited.add((row, col, cur_keys))
            

                if len(cur_keys) == keys:
                    return moves

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    new_keys = set(cur_keys)

                    if is_valid(new_row, new_col):

                        if grid[new_row][new_col] in "ABCDEF" and grid[new_row][new_col].lower() not in new_keys:
                            continue

                        if grid[new_row][new_col].islower() and grid[new_row][new_col] != '.':
                            new_keys.add(grid[new_row][new_col])


                        queue.append((new_row, new_col, tuple(new_keys), moves + 1))
                    
                    
        return -1
            
            
            
                    
                    