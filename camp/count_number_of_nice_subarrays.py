class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]

        prefix = defaultdict(int)
        prefix[0] = 1

        subarrays = 0
        running = 0
        for i in nums:
            running += i
            subarrays += prefix[running - k]
            prefix[running] += 1
        return subarrays
