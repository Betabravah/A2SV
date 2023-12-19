class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 1
        i = 0
        got = False
        while  i < len(nums):
            if nums[i] < 0 and i+1 < len(nums) and nums[i+1] < 0:
                ans *= (nums[i] * nums[i+1])
                i += 1
                got = True
                
            elif nums[i] > 0:
                ans *= nums[i]
                got = True
                
            i += 1
            
        return ans if got else nums[-1]
                