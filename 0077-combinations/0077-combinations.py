class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def find(temp, idx):
            if len(temp) == k:
                combinations.append(temp)
                return
            if idx == n+ 1:
                return
            find(temp+[idx], idx+1)
            find(temp, idx+1)
        
        find([], 1)
        return combinations
            