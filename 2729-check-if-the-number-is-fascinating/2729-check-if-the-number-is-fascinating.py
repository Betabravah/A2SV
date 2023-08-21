class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(n * 2) + str(n * 3)
        
        if len(n) > 9:
            return False
        
        for i in range(1, 10):
            if str(i) not in n:
                return False
            
        return True
            