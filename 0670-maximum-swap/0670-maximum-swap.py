class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = list(str(num))
        digits = {j:i for i, j in enumerate(num)}
        
        
        for i in range(len(num)):
            cur_dig = num[i]
            
            for j in range(9, int(cur_dig), -1):
                if str(j) in digits and digits[str(j)] > i:
                    num[i], num[int(digits[str(j)])] = num[int(digits[str(j)])], num[i]
                    return int(''.join(num))
                    
        
        return int(''.join(num))  
                