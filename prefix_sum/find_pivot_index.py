class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lst1 = [None] * len(nums)
        lst2 = [None] * len(nums)
        x = y = 0
        for i in range(len(nums)):
            x += nums[i]
            y += nums[len(nums) - 1 - i]
            lst1[i] = x
            lst2[len(nums) - 1 -i] = y
        
        for i in range(len(nums)):
            if lst1[i] == lst2[i]:
                return i
         
        return -1
            