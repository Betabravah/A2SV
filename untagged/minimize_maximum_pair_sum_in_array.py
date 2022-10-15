class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(len(nums)):
            maxSum = max(maxSum, nums[i] + nums[len(nums)-1 - i])
            
        return maxSum
