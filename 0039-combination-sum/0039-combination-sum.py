class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        n = len(candidates)
        def find(idx, path, total):
            if total > target:
                return
            if total == target:
                comb.append(path.copy())
                return            
            
            for i in range(idx, n):
                path.append(candidates[i])
                find(i, path, total + candidates[i])
                path.pop()
                
            
            
        find(0, [], 0)
        return comb
                