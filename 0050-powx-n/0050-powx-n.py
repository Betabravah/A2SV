class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n == -1:
                return 1 / x
            num =  1
            
            if n % 2 != 0:
                num = x
            return self.myPow(x * x, n // 2) * num
        
        return pow(x, n)

                