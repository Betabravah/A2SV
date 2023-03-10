class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        n = len(nums)
        def backtrack(idx, path):
            if idx == n:
                return
            # subsets.append(path.copy())
            path.append(nums[idx])
            for i in range(idx+1, n):
                backtrack(i, path)
                path.pop()
            subsets.append(path.copy())

                
        for i in range(n):
            backtrack(i, [])
        
        return subsets
                
        