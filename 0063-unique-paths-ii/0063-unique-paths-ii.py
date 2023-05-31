class Solution:
    def uniquePathsWithObstacles(self, obstacles: List[List[int]]) -> int:
        if obstacles[-1][-1] == 1:
            return 0
        
        
        rows, cols = len(obstacles), len(obstacles[0])
        ans = [[0 for i in range(cols)] for j in range(rows)]
        ans[-1][-1] = 1
        
        
        for row in range(rows-1, -1 ,-1):
            for col in range(cols-1, -1, -1):
                
                if obstacles[row][col] == 1:
                    continue
                    
                if 0 <= row + 1 < rows:
                    ans[row][col] += ans[row+1][col]
                    
                if 0 <= col + 1 < cols:
                    ans[row][col] += ans[row][col+1]
                    
                    
        return ans[0][0]
                    
                
                    
                
                