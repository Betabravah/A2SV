class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0:1}
        prefix = count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            diff = prefix - k

            if diff in prefix_count:
                count += prefix_count[diff]
            prefix_count[prefix] = 1 + prefix_count.get(prefix, 0)

        return count
