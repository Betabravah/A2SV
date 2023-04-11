class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        for i in range(len(nums)):
            
            
            while nums[i] - 1 != i and 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                    

            i += 1
            
            
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
            
        return len(nums) + 1
                
                
        
            
            
        