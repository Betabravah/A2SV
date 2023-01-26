class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        _dict = {}
        for rowIdx, row in enumerate(matrix):
            for colIdx, col in enumerate(row):
                diff = colIdx - rowIdx
                if diff in _dict.keys():
                    if _dict[diff] != col:
                        return False
                else:
                    _dict[diff] = col
        return True
