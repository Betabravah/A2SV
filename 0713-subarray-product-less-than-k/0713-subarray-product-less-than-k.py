class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left = 0
        prod = 1
        ans = [i for i in range(n)]
        
        for i in range(n):
            prod *= nums[i]
            
            while left <= i and prod >= k:
                prod //= nums[left]
                left += 1
                
            ans[i] = i - left + 1
            
        res = sum(ans)
        
        return res
