class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
                    
        
        for row in matrix:
            row.sort(reverse=True)
                
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, matrix[i][j] * (j + 1))
                
        return ans
                