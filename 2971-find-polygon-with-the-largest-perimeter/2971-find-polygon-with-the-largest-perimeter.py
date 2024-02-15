class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        total = sum(nums)
        
        for i in range(n-1, -2, -1):
            total -= nums[i]
            
            if total > nums[i]:
                return total + nums[i]
            
        return -1
            
            