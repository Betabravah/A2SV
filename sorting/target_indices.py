class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        nums.sort()
        if target in nums:
            index = nums.index(target)
            for i in range(index, len(nums)):
                if nums[i] == target:
                    indices.append(i)
        return indices