class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _sum = sum(nums)
        expectedSum = 0

        for i in range(len(nums)+1):
            expectedSum += i

        return expectedSum - _sum
