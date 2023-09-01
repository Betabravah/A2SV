class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        ans = 0
        for i in freq:
            if freq[i-1]:
                ans = max(ans, freq[i-1] + freq[i])
            if freq[i+1]:
                ans = max(ans, freq[i] + freq[i+1])
            
        return ans
            