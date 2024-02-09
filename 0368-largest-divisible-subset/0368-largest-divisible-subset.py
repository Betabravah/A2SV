class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        
        maxL, maxIndex = 1, 0
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
                    if dp[i] > maxL:
                        maxL = dp[i]
                        maxIndex = i
              
        
        
        num = nums[maxIndex]
        ans = []         
        for i in range(maxIndex, -1, -1):
            if num % nums[i] == 0 and dp[i] == maxL:
                ans.append(nums[i])
                maxL -= 1
                num = nums[i]
                
                
        return ans
                    
                    
            
    
        
        
        
        
        
                    