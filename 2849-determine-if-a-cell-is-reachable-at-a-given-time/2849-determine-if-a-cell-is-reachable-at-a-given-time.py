class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        max_distance = max(abs(fy - sy), abs(fx - sx))
        
        if sx == fx and sy == fy and t == 1:
            return False
        
        if t >= max_distance:
            return True
        
        return False