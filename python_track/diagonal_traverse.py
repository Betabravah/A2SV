class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)        
        col = len(mat[0])
        diagonal = [mat[0][0]]
        
        cur = [0,0]
        direction = 'up'
        while cur != [row-1, col-1]:
            if direction == 'up':
                cur[0] -= 1
                cur[1] += 1
                if cur[0] < 0 and 0 <= cur[1] <= col-1:
                    cur[0] += 1
                    diagonal.append(mat[cur[0]][cur[1]])
                    direction = 'down'
                elif cur[0] < 0 and cur[1] > col-1:
                    cur[0] += 2
                    cur[1] -= 1
                    diagonal.append(mat[cur[0]][cur[1]])
                    direction = 'down'
                elif cur[1] > col-1 and 0 <= cur[0] <= row-1:
                    cur[0] += 2
                    cur[1] -= 1
                    diagonal.append(mat[cur[0]][cur[1]])
                    direction = 'down'
                else:
                    diagonal.append(mat[cur[0]][cur[1]])
                    
            else:
                cur[0] += 1
                cur[1] -= 1
                if cur[1] < 0 and 0 <= cur[0] <= row-1:
                    cur[1] += 1
                    diagonal.append(mat[cur[0]][cur[1]])
                    direction = 'up'
                elif cur[0] > row-1 and cur[1] < 0:
                    cur[0] -= 1
                    cur[1] += 2
                    diagonal.append(mat[cur[0]][cur[1]])
                    direction = 'up'
                elif cur[0] > row-1 and 0 <= cur[1] <= col-1:
                    cur[0] -= 1
                    cur[1] += 2
                    diagonal.append(mat[cur[0]][cur[1]])
                    direction = 'up'
                else:
                    diagonal.append(mat[cur[0]][cur[1]])
            
        return diagonal
