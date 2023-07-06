class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
                    
        def in_bound(row, col):
            return 0 <= row < 2 and 0 <= col < 3
        
        
        def get_neighbours(board):
            neighbours = []
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        r, c = i, j
                        
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change
                
                if in_bound(new_row, new_col):
                    new_board = [row[:] for row in board]
                    new_board[r][c] = new_board[new_row][new_col]
                    new_board[new_row][new_col] = 0
                    
                    neighbours.append(new_board)
                    
            return neighbours
            
                    
        queue = deque([(board, 0)])            
        visited = set()
        visited.add(tuple(tuple(row) for row in board))
        
        while queue:
            board, step = queue.popleft()
            
            if board == [[1,2,3],[4,5,0]]:
                return step
            
            for neigh in get_neighbours(board):
                temp = tuple(tuple(row) for row in neigh)
                if temp not in visited:
                    visited.add(temp)
                    queue.append((neigh, step + 1))
                    
                    
        return -1
                    
                    
                    
        
                    