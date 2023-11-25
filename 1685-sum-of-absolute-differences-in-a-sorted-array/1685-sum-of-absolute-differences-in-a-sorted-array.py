class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)
        
    
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
            
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]
            
        
        ans = []
        for i in range(n):
            ans.append((suffix[i+1] - (nums[i]) * (n-1-i)) + ((nums[i]) * i - prefix[i]))
            
        return ans