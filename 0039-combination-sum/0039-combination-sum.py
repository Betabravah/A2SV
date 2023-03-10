class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        n = len(candidates)
        def find(idx, path, total):
            if idx == n:
                return
            if total > target:
                return
            if total == target:
                comb.append(path.copy())
                return            
            path.append(candidates[idx])
            find(idx, path, total + candidates[idx])
            path.pop()
            find(idx+1, path, total)
            
                
                
                
            
            
        find(0, [], 0)
        return comb
                