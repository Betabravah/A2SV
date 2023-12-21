class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort()
        
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            
            ans = max(ans, p2[0] - p1[0])
            
        return ans