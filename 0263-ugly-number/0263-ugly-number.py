class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        
        divisors = [2, 3, 5]
        
        for div in divisors:
            while num % div == 0:
                num //= div
                
        return num == 1