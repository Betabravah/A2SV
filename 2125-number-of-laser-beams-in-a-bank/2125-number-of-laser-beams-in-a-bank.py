class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = ans = 0
        
        for i in range(len(bank)):
            cur = bank[i].count('1')
            
            ans += (cur * last)
            
            if cur > 0:
                last = cur
                
        return ans