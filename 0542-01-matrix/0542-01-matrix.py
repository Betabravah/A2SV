class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(mat)
        n = len(mat[0])
        
        
        def in_bound(row, col):
            return 0 <= row < m and 0 <= col < n
        
                        
                        
        queue = deque() 
        visited = set()
        output = [[float(inf) for _ in range(len(mat[0]))] for i in range(len(mat))]
        
        for i in range(m):
            for j in range(n):
                
                if mat[i][j] == 1:
                    
                    for rc, cc in directions:
                        new_row, new_col = rc + i, cc + j
                        
                        if in_bound(new_row, new_col) and mat[new_row][new_col] == 0:
                            queue.append((i, j, 1))
                            output[i][j] = 1
                            visited.add((i, j))
                            
                else:
                    output[i][j] = 0
                    
                    
        
        


        while queue:
            cur_row, cur_col, depth = queue.popleft()
            output[cur_row][cur_col] = depth
            

            for row_change, col_change in directions:
                new_row = cur_row + row_change
                new_col = cur_col + col_change

                
                if in_bound(new_row, new_col) and (new_row, new_col) not in visited and mat[new_row][new_col] == 1:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, depth + 1))
                            
                        
        
        return output
        
                        
                        
                        
                        
                        
                    