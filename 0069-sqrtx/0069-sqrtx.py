class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid == x:
                return mid
            else:
                low = mid + 1
            
        return high