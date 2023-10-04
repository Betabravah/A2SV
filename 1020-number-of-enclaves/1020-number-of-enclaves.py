class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        
        stack = []
        count = 0
        visited = set()
        temp = 0
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    count += 1
                    
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        stack.append([i, j])
                        visited.add((i, j))
                        
                        
        def is_bound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        
        def get_neighbours(row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            neigh = []
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_bound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    neigh.append((new_row, new_col))
                    
            return neigh
        
        
        
        while stack:
            
            row, col = stack.pop()
            temp += 1
            
            for r, c in get_neighbours(row, col):
                visited.add((r, c))
                stack.append((r, c))
                
        return count - temp