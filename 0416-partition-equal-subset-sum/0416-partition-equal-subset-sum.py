class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total // 2
        memo = defaultdict(bool)
        
        
        def backtrack(index, cur):
            if index >= len(nums):
                return False
            
            if cur > half:
                return False
            
            if cur == half:
                return True
            
            if (index, cur) not in memo:
                memo[(index, cur)] = backtrack(index+1, cur + nums[index]) or backtrack(index+1, cur)
            
            return memo[(index, cur)]
            
              
            
        return backtrack(0, 0)
                