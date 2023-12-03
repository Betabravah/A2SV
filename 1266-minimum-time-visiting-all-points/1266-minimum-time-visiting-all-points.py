class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(points) - 1):
            curx, cury = points[i]
            targetx, targety = points[i+1]
            
            ans += (max(
                abs(targetx - curx),
                abs(targety - cury)
            ))
            
        return ans