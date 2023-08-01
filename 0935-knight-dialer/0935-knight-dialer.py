class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
    
        mod = (10**9 + 7)
        for _ in range(n-1):
            new_dp = [0] * 10
            
            for i in range(10):
                for j in jump[i]:
                    new_dp[i] += dp[j]
                    
            dp = new_dp
        
        return sum(dp) % mod