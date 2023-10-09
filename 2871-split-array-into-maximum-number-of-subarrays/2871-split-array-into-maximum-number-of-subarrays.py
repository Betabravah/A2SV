class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total_score = nums[0]
        
        for i in nums:
            total_score &= i
            
        if total_score > 0:
            return 1
        
        
        score = nums[0]
        ans = 0
        
        for idx, i in enumerate(nums):
            score &= i
            
            if score == 0:
                ans += 1
                
                if idx+1 < len(nums):
                    score = nums[idx+1]
                
        return ans