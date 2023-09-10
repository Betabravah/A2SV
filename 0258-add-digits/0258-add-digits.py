class Solution:
    def addDigits(self, num: int) -> int:
            
        def add(num):
            if num < 10:
                return num

            new_num = 0
            while num:
                new_num += (num % 10)
                num //= 10

            return add(new_num)
            
        return add(num)
        
        