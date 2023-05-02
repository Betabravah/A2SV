class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        stack = []
        visited = set()
        
        for i in range(m):
            
            if i == 0 or i == m - 1:
                for j in range(n):
                    if board[i][j] == 'O':
                        stack.append((i, j))
                        visited.add((i, j))
            
            
            else:
                
                if board[i][0] == 'O':
                    stack.append((i, 0))
                    visited.add((i, 0))


                if board[i][-1] == 'O':
                    stack.append((i, n-1))
                    visited.add((i, n-1))
                
                
            
            
            
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and board[row][col] == 'O'
        
        
        
        while stack:
            row, col = stack.pop()
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    stack.append((new_row, new_col))
                    
                    
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
                    
                    
                    
                    
            
            
            
            
            
            
            