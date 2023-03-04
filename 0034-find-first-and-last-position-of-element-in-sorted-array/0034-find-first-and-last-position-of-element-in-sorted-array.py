class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target and nums[high] > target:
                high -= 1
            elif nums[mid] == target and nums[low] < target:
                low += 1
            elif nums[low] == nums[high] == target:
                break
        else:
            return [-1, -1]
                
        return [low, high]