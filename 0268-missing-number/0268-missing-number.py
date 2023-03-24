class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        real = 0
        for i in range(1, n+1):
            real += i
            
        return real - total