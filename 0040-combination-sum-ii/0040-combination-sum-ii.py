class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(idx, path, total):
            
            if total > target:
                return
            
            if total == target:
                ans.append(path.copy())
                return
            
            
            else:
            
                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates[i-1]:
                        continue
                        
                    backtrack(i+1, path + [candidates[i]], total + candidates[i])

                
        ans = []
        candidates.sort()
        backtrack(0, [], 0)
        return ans