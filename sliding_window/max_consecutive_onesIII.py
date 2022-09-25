class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = first = size = 0
        for last in range(len(nums)):
            if nums[last] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[first] == 0:
                    zeroes -= 1
                first += 1

            size = max(size, (last - first + 1))

        return size