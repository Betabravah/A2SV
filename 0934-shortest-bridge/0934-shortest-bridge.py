class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        queue = deque()
        visited = set()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def is_bound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        
        def dfs(row, col):
            stack = [(row, col)]
            
            while stack:
                row, col = stack.pop()
                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if is_bound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, 0))
                        stack.append((new_row, new_col))
                        
                        
                        
                        
        got = False
        for i in range(n):
            for j in range(n):
                
                if grid[i][j] == 1:
                    queue.append((i, j, 0)) 
                    visited.add((i, j))
                    dfs(i, j)
                    got = True
                    break
                    
            if got:
                break
        
        
        
        
        while queue:
            row, col, depth = queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if is_bound(new_row, new_col) and (new_row, new_col) not in visited:
                    if grid[new_row][new_col] == 1:
                        return depth
                    
                    queue.append((new_row, new_col, depth+1))
                    visited.add((new_row, new_col))

        
        
        
        
        