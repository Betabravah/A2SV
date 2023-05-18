class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = [i for i in range(n+1)]
        rank = [1] * (n + 1)
        min_score = [inf for i in range(n+1)]
        
        
        def find(node):
            if root[node] != node:            
                root[node] = find(root[node])
            return root[node]
            
        
        for i, j, distance in roads:
            
            repi, repj = find(i), find(j)
            
            ranki, rankj = rank[repi], rank[repj]
            minn = min(min_score[root[repi]], min_score[root[repj]], distance)
            
            
            if rank[repi] == rank[repj]:
                rank[repi] += 1
                
            if rank[repi] < rank[repj]:
                root[repi] = repj
                min_score[repj] = minn
            else:
                root[repj] = repi
                min_score[repi] = minn
                
                
        return min_score[find(1)]
                
                
                
                
            