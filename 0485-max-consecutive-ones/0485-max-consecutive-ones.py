class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left = right = ans = 0
        while right < len(nums):
            if nums[right] == 0:
                left = right + 1
            ans = max(ans, right - left + 1)
            right += 1
            
        return ans