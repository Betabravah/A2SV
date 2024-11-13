class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        cur = ans = 0
        
        for i in range(len(nums)):
            cur += nums[i]
            
            ans += prefix[cur-k]
            prefix[cur] += 1
            
            
        return ans