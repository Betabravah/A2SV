class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = defaultdict(int)
        
        
        def dp(row, col):
            if row >= len(triangle):
                return 0
            
            if (row, col) not in memo:
                memo[(row, col)] = min(dp(row+1, col), dp(row+1, col+1)) + triangle[row][col]
                
            return memo[(row, col)]
        
        
        return dp(0, 0)
            
            
            