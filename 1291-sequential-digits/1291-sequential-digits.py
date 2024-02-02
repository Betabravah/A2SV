class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []
        
        for i in range(1, 10):
            num = i
            next_dig = i + 1
            
            while next_dig <= 9 and num < high:
                num = num * 10 + next_dig
                
                if low <= num <= high:
                    ans.append(num)
                    
                next_dig += 1
        
        ans.sort()
        return ans