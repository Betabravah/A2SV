class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = col = 0
        try:
            while matrix[row][col] < target and matrix[row][-1] < target:
                row += 1
        except:
            return False
            
        try:
            while matrix[row][col] != target:
                col += 1
        except:
            return False
            
        return True

# Time complexity = O(n + m) for n rows and m columns
