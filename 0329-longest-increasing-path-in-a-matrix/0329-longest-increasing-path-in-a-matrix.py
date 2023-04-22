class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isvalid(row, col, cur):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] > cur
        
        _dict = defaultdict(int)
        
        def dfs(row, col, cur):
            
            if not isvalid(row, col, cur):
                return 0
            
            if _dict[(row, col)] != 0:
                return _dict[(row, col)]
            
            res = 1
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if isvalid(new_row, new_col, matrix[row][col]):
                    res = max(res, 1 + dfs(new_row, new_col, matrix[row][col]))
                              
            _dict[(row, col)] = res
            
            return res
                              
                              
        max_length = 0       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_length = max(max_length, dfs(i, j, -float('inf')))
                
        return max_length
                    
                