class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * (len(nums))
        dp[0] = True
        
        for i in range(len(nums)):
            
            if dp[i]:
            
                for j in range(i+1, i + nums[i] + 1):
                    if j < len(nums):
                        dp[j] = True
                        
                    else:
                        return True
                        
        return dp[-1]
                    
                