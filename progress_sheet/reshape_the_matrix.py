class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        count = 0

        if rows * cols != r * c:
            return mat

        reshaped = [[0 for i in range(c)] for j in range(r)]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                reshaped[count // c][count % c] = mat[row][col]
                count += 1

        return reshaped
