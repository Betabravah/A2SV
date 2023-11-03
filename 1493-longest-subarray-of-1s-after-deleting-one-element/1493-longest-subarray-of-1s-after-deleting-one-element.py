class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = ans = 0
        prev = -1
        
        while right < len(nums):
            if nums[right] == 0:
                left = prev + 1
                    
                prev = right
                
            
            ans = max(ans, right - left)
            
            right += 1
            
        return ans