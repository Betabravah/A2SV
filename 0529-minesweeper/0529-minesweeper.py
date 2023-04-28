class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        
        def isvalid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        
        def dfs(row, col):
            
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
                
            elif board[row][col] == 'E':
                
                neighbour_mine = 0
                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if isvalid(new_row, new_col) and board[new_row][new_col] == 'M':
                        neighbour_mine += 1
                        
                        
                if neighbour_mine:
                    cur = board[row][col]
                    
                    if isinstance(cur, int):
                        board[row][col] = str(neighbour_mine + int(cur))
                        
                    else:
                        board[row][col] = str(neighbour_mine)
                        
                else:
                    board[row][col] = 'B'
                    
                    for row_change, col_change in directions:
                        new_row = row + row_change
                        new_col = col + col_change

                        if isvalid(new_row, new_col):
                            dfs(new_row, new_col)
                         
        
        dfs(click[0], click[1])
        return board
                        
                        
            
                    
                    
                    
                    
                    
                    
                    
                    