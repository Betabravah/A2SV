class Solution:
    def totalMoney(self, n: int) -> int:
        monday = prev_day = 0
        ans = 0
        
        for i in range(n):
            if i % 7 == 0:
                monday += 1
                ans += monday
                prev_day = monday
                
            else:
                prev_day += 1
                ans += prev_day
            
        return ans