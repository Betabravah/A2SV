class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subseq = set()
        path = []
        def backtrack(idx):
            
            if idx >= len(nums):
                return
            
            tmp = path[-1] if path else None
            
            
            if tmp == None or nums[idx] >= tmp:
                path.append(nums[idx])
                
                if len(path) >= 2:
                    subseq.add(tuple(path.copy()))
                    
                backtrack(idx+1)
                path.pop()
            backtrack(idx+1)
                   
                
            return subseq
        return backtrack(0)
            