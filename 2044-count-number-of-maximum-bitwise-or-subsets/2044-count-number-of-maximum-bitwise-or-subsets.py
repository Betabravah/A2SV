class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for num in nums:
            maximum |= num
                
        
        def calc_or(path):
            # print(path)
            ans = 0
            for num in path:
                ans |= num
                
            return ans
        
        
        def backtrack(idx, path):
            # print(path)
            nonlocal count
            
            if calc_or(path) == maximum:
                count += 2 ** (len(nums) - idx)
                return
            
            if idx == len(nums):
                return
            
            
            backtrack(idx + 1, path + [nums[idx]])
            backtrack(idx + 1, path)
                
        
        
        count = 0
        backtrack(0, [])
        
        return count