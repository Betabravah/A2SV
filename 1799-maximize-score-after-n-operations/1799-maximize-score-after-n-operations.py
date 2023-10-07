class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def backtrack(nums, k):
            
            ans = 0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    new_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    
                    ans = max(ans, k * gcd(nums[i], nums[j]) + backtrack(new_nums, k+1))
                    
            return ans
        
        return backtrack(tuple(nums), 1)
