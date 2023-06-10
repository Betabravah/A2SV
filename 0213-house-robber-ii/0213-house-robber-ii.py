class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = defaultdict(int)
        
        def dp(n):
            if n == 0:
                return nums[0]
            
            if n == 1 :
                return max(nums[1], nums[0])
            
            if n not in memo:
                memo[n] = max(dp(n-1), dp(n-2) + nums[n])
                
            return memo[n]
        
        case_1 = dp(len(nums) - 2)
        memo = defaultdict(int)
        nums.pop(0)
        case_2 = dp(len(nums) - 1)
        return max(case_1, case_2)
        
        