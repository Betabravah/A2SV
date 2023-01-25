class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        ctr = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left+1] = nums[right]
                ctr += 1
                right += 1
                left += 1
        return ctr
