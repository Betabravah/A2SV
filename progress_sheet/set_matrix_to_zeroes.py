class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for rowIdx, row in enumerate(matrix):
            for colIdx, col in enumerate(matrix[rowIdx]):
                if col == 0:
                    rows.append(rowIdx)
                    cols.append(colIdx)
        
        for row in rows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
