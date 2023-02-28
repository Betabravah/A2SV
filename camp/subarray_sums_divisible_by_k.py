class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        running_sum = sub_arrays = 0
        for num in nums:
            running_sum = (running_sum + num) % k
            prefix_count = prefix[running_sum]
            sub_arrays += prefix_count
            prefix[running_sum] += 1

        return sub_arrays
