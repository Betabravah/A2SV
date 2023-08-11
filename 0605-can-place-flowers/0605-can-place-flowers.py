class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        if len(nums) == 1 and nums[0] == 0 and n <= 1:
            return True
        
        
        if len(nums) >= 2 and nums[0] == 0 and nums[1] == 0:
            nums[0] = 1
            n -= 1
            
        for i in range(1, len(nums)-1):
            if nums[i] == 0 and nums[i-1] == nums[i+1] == 0:
                nums[i] = 1
                n -= 1
        if len(nums) >= 2 and nums[-1] == nums[-2] == 0:
            n -= 1
                
        return n <= 0