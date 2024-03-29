class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = ans = 0
        n = len(nums)
        count = defaultdict(int)
        
        for i in range(n):
            count[nums[i]] += 1
            
            while count[nums[i]] > k:
                count[nums[left]] -= 1
                left += 1
                
            ans = max(ans, i - left + 1)
            
        return ans