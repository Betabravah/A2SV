class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                summ = nums[i] + nums[j]
                
                index = bisect_left(nums, summ)
                
                if index > j:
                    ans += (index - j - 1)
                    
                    
        return ans