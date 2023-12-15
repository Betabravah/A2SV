class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = defaultdict(int)
        
        for i, j in paths:
            outdegree[i] += 1
            
            
        for i, j in paths:
            if outdegree[i] == 0:
                return i
            if outdegree[j] == 0:
                return j