class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        low = high = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                high = low + 1
                
            elif nums[i] < nums[i - 1]:
                low = high + 1
                
                
        return max(low, high)