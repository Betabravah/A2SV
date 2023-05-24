class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {tuple(i): tuple(i) for i in stones}
        
        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
                
            return root[node]
        
            
        def union(x, y):
            
            rootx, rooty = find(x), find(y)
            
            if rootx == rooty:
                return
            
            if rootx < rooty:
                root[rooty] = rootx
                
            else:
                root[rootx] = rooty
                
                
                
        for i in root:
            for j in root:
                if i[0] == j[0] or i[1] == j[1]:
                    union(i, j)
                    
                    
        roots = set()
        for i in root:
            roots.add(find(i))
            
        return len(stones) - len(roots)
        