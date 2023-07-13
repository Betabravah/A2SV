class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * (length + 1)
        
        
        for i in range(length - 1, -1, -1):
            point, skip = questions[i]
            
            next = i + skip + 1
            next = length if next >= length else next
                
            dp[i] = max(dp[i+1], dp[next] + point)
            
            
        return dp[0]