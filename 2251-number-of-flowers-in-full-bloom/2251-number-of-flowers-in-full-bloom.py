class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        starts = []
        ends = []
        
        for s, e in flowers:
            starts.append(s)
            ends.append(e)
            
        starts.sort()
        ends.sort()
        
        ans = []
        for i in people:
            started = bisect_right(starts, i)
            ended = bisect_left(ends, i)
            
            ans.append(started - ended)
            
        return ans