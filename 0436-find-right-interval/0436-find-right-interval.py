class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        
        for idx, interval in enumerate(intervals):
            start.append([interval[0], idx])
            
        
        start.sort()
        
        output = []
        for i, j in intervals:
            index = bisect_left(start, [j, 0])
            
            if index >= len(intervals):
                index = -1
            else:
                _, index = start[index]
                
            output.append(index)
            
        return output
            