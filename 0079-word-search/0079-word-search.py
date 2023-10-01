class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_bound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def get_neighbours(row, col):
            neighbours = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if is_bound(new_row, new_col):
                    neighbours.append((new_row, new_col))
                    
            return neighbours
        
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if board[row][col] != word[index]:
                return False
            
            original_char = board[row][col]
            board[row][col] = "#"
            
            for nrow, ncol in get_neighbours(row, col):
                if backtrack(nrow, ncol, index+1):
                    return True
                
            board[row][col] = original_char
            
            return False
        
        if len(board) == len(board[0]) == 1 and word == board[0][0]:
            return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False