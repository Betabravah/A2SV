class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        def get_range(left, right):
            if nums[left] == nums[right]:
                return str(nums[left])
            return str(nums[left]) + "->" + str(nums[right])
        
        
        left = 0
        ans = []
        for right in range(1, len(nums)):
            
            if nums[right] > nums[right-1] + 1:
                
                ans.append(get_range(left, right-1))
                
                left = right
                
        ans.append(get_range(left, len(nums)-1)) 
        return ans
                    
                    
                