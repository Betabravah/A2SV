class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []
        for _ in range(len(grid) - 2):
            maxLocal.append([0] * (len(grid) - 2))
        length = len(maxLocal)
        for row in range(1, length + 1):
            for col in range(1, length + 1):
                maxLocal[row-1][col-1] = max( 
                grid[row-1][col-1], grid[row-1][col], grid[row-1][col+1],
                grid[row][col-1], grid[row][col], grid[row][col+1],
                grid[row+1][col-1], grid[row+1][col], grid[row+1][col+1])
        return maxLocal 
