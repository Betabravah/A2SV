class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append('0')
        ptr = 0
        
        while ptr < len(nums):
            if isinstance(nums[ptr], int):
                if nums[ptr] != ptr:
                    idx = nums[ptr]
                    nums[ptr], nums[idx] = nums[idx], nums[ptr]
                    
                else:
                    ptr += 1
            else:
                ptr += 1
                
        for i in range(len(nums)):
            if not isinstance(nums[i], int):
                return i
        
        
        