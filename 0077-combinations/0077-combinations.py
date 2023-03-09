class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def find(temp, idx):
            if len(temp) == k:
                combinations.append(temp)
            else:     
                for i in range(idx, n+1):
                    find(temp+[i], i+1)
        
        find([], 1)
        return combinations
            