class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        ans = 0
        for num in freq:
            if freq[num] == 1:
                ans += num
                
        return ans