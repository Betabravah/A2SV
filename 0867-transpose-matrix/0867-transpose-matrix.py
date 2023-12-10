class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[None] * len(matrix) for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]
                
        return ans