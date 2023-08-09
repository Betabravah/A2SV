class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nearest = {}
        
        for i in range(len(nums)):
            if nums[i] in nearest:
                if abs(nearest[nums[i]] - i) <= k:
                    return True
                else:
                    nearest[nums[i]] = i
            
            nearest[nums[i]] = i
                
                
        return False