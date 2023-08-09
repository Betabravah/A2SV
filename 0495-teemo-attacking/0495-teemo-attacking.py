class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        ans = duration
        for i in range(1, len(timeSeries)):
            ans += min(0, timeSeries[i] - timeSeries[i-1] - duration)
            ans += duration
                
        return ans