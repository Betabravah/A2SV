class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_so_far = ans = 0
        
        for i in range(n):
            ans = max(ans, max_so_far + values[i] - i)
            max_so_far = max(max_so_far, values[i] + i)
        
        return ans