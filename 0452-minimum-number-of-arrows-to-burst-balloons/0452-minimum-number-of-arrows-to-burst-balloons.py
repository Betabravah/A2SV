class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        ans = []
        start = points[0][0]
        last = points[0][1]
        ctr = 1
        print(points)
        
        for i, j in points:
            if i <= last:
                start = max(start, i)
                last = min(last, j)
                
            else:
                ans.append([i,j])
                start = i
                last = j
                ctr += 1
                print(i, j)
            
            
        return ctr