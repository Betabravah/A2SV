class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        
        heap = []
        heappush(heap, (grid[0][0], 0, 0))
        visited.add((0, 0))
        
        
        def is_bound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while True:
            val, row, col = heappop(heap)
            ans = max(ans, val)
            
            if val == grid[-1][-1]:
                return ans
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_bound(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    heappush(heap, (grid[new_row][new_col], new_row, new_col))
            
                        