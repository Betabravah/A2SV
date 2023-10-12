class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            
            heappush(heap, (dist, x, y))
            
            
        ans = []
        for i in range(k):
            d, x, y = heappop(heap)
            
            ans.append([x, y])
            last = d
        
        
        while heap:
            d, x, y = heappop(heap)
            
            if d == last:
                ans.append([x, y])
            else:
                break
                
                
        return ans