class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols) for _ in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols):
                dp[i][j] = dp[i-1][j]
                
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                
                if j+1 < cols:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                
                dp[i][j] += matrix[i][j]
                        
                                  
        return min(dp[-2])