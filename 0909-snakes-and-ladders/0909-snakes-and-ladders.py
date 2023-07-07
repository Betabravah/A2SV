class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def num2rc(num):
            row = n - 1 - (num - 1) // n
            col = (num - 1) % n
            
            if (n - row) % 2 == 0:
                col = n - 1 - col
            
            return row, col
        
        
        queue = deque([(1, 0)])
        visited = set()
        
        while queue:
            cell, step = queue.popleft()
            
            if cell == n * n:
                return step
            
            for i in range(1, 7):
                new_cell = cell + i
                
                if new_cell > n * n:
                    break
                    
                if new_cell not in visited:
                    visited.add(new_cell)
                    
                    row, col = num2rc(new_cell)
                    if board[row][col] != -1:
                        new_cell = board[row][col]
                    queue.append((new_cell, step + 1))
                        
        return -1
        
        
        
        
        
        