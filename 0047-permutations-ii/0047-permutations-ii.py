class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path, new_nums):
            nonlocal ans
            
            if len(path) == len(nums):
                _tuple = tuple(path)
                
                if _tuple not in seen:
                    ans.append(path.copy())
                    seen.add(_tuple)
                return
            
            for i in range(len(new_nums)):
                backtrack(path + [new_nums[i]], new_nums[:i] + new_nums[i+1:])
                
        ans = []
        seen = set()
        backtrack([], nums)
        return ans
                
                
                