class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        
        def rob(n):
            if n < 0:
                return 0
            
            if n == 1 or n == 0:
                return nums[n]
            
            if n not in memo:
                memo[n] = max(rob(n - 2), rob(n - 3)) + nums[n]
                
            return memo[n]
        
        
        return max(rob(len(nums) - 1), rob(len(nums) - 2))
                