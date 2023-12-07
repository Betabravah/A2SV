class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def get_power(num, step):
            if num == 1:
                return step
            
            if num % 2:
                return get_power(3*num + 1, step+1)
            
            return get_power(num / 2, step+1)
        
        ans = []
        for i in range(lo, hi+1):
            ans.append((get_power(i, 0), i))
            
            
        ans.sort()
        return ans[k-1][1]
            
        
            
            