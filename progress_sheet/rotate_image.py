class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()
