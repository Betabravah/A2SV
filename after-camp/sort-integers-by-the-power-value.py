class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def steps(n):
            if n == 1:
                return 0
            
            if n % 2:
                return steps(3 * n +1) + 1
            return steps(n // 2) + 1
        
        
        nums = [i for i in range(lo, hi+1)]
        
        nums.sort(key=lambda x: steps(x))
        
        return nums[k-1]