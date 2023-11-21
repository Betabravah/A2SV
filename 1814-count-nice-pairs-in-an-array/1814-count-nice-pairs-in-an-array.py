class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        
        for i in nums:
            rev = int(str(i)[::-1])
            
            ans += count[i - rev]
            count[i - rev] += 1
            
        return ans % (10**9 + 7)