class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for i in freq:
            if freq[i] == 1:
                return -1
            else: 
                ans += (freq[i] + 2) // 3
            
        return ans