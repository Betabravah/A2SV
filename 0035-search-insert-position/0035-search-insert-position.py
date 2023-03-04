class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect_left(nums, target)
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low