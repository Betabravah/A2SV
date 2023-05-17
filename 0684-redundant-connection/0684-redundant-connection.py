class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = {}
        
        def find(node):
            rep = root.get(node, node)
            if rep == node:
                return node
            
            root[node] = find(root[node])
            return root[node]
            
        
        for i, j in edges:
            
            repi, repj = find(i), find(j)
            if repi == repj:
                return [i, j]
            
            
            root[repj] = repi
                
                
