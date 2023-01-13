class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                nums[idx] *= 2
                nums[idx + 1] = 0
        
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
    
        return nums
