class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [eval(i) for i in nums]
        nums.sort()
            
        return str(nums[len(nums) - k])
