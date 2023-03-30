class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        
        while i < len(nums):
            correct_idx = nums[i] - 1
            
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
            else:
                i += 1
                
        missing = [] 
        for i in range(len(nums)):
            if nums[i] != i+1:
                missing.append(i+1)
                
        return missing