class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = []
        
        for i in range(len(dist)):
            times.append(dist[i] / speed[i])
            
        times.sort()
            
        # 0.6, 0.67, 2
        # 1, 3, 4
        cur = ans = prev = 0
        for i in times:
            if i > prev:
                ans += 1
                prev += 1
                
            else:
                break
        
        return ans
        