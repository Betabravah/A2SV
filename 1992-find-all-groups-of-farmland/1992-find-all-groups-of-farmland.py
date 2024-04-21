class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def is_bound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        
        def traverse(row, col):
            nonlocal right_most
            nonlocal bottom_most
            
            right_most = max(right_most, col)
            bottom_most = max(bottom_most, row)
            
            directions = [(0, 1), (1, 0)]
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_bound(new_row, new_col) and land[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    traverse(new_row, new_col)
                    visited.add((new_row, new_col))
                    
                    
        rows = len(land)
        cols = len(land[0])
        ans = []
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    right_most = j
                    bottom_most = i
                    
                    traverse(i, j)
                    
                    ans.append([i, j, bottom_most, right_most])
                    
        return ans