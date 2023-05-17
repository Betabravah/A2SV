class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            if root[node] == node:
                return node
            
            root[node] = find(root[node])
            return root[node]
            
        
        for i, j in edges:
            
            repi, repj = find(i), find(j)
            
            ranki, rankj = rank[repi], rank[repj]
            
            
            if rank[repi] == rank[repj]:
                rank[repi] += 1
                
            if rank[repi] < rank[repj]:
                root[repi] = repj
            else:
                root[repj] = repi
                
                
        return find(source) == find(destination)
                
                
            
