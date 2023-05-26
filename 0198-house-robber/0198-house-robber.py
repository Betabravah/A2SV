class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        
        def rob(n):
            if n == 0:
                return nums[0]
            
            if n == 1 :
                return max(nums[1], nums[0])
            
            if n not in memo:
                memo[n] = max(rob(n-1), rob(n-2) + nums[n])
                
            return memo[n]
        
        
        return rob(len(nums) - 1)
                