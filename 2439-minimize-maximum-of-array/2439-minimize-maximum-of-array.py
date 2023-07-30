class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ave = 0
        temp = 0
        
        for i in range(len(nums)):
            temp += nums[i]
            ave = max(ave, ceil(temp / (i+1)))
            
        return ave