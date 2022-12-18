class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def sum_hourglass(i, j): # returns sum of hoursglass with center at grid[i][j]
            return sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])

        res = 0
        for row in range(1, m-1): # iterate through the posible centers of hourglass
            for col in range(1, n-1):
                res = max(res, sum_hourglass(row, col))

        return res