class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))
        
        ans = float('inf')
        
        for i in range(len(nums)):
            
            right = nums[i] + (n - 1)
            right_index = bisect_right(nums, right)
            count = right_index - i
            
            ans = min(ans, n - count)
          
                
        return ans