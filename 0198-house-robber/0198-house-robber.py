class Solution:
    def rob(self, nums: List[int]) -> int:
        left = right = 0
        
        for i in nums:
            temp = max(left + i, right)
            left = right
            right = temp
            
        return temp