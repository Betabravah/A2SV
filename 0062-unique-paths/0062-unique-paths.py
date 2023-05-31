class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows, cols = m, n
        ans = [[0 for _ in range(cols)] for j in range(rows)]
        ans[rows-1][cols-1] = 1
        
        
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                
                if 0 <= row + 1 < rows:
                    ans[row][col] += ans[row + 1][col]
                    
                if 0 <= col + 1 < cols:
                    ans[row][col] += ans[row][col + 1]
                    
                    

        return ans[0][0]
            
            
            
            