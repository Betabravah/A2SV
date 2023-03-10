class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_greater = [-1] * len(nums)
        nums.extend(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if i < len(next_greater) and stack:
                next_greater[i] = stack[-1]
                
            stack.append(nums[i])
            
             
        return next_greater
            
                    

                    
