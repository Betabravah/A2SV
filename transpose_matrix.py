class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transp = [[None for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transp[col][row] = matrix[row][col]

        return transp