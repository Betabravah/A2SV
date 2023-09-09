class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
                
            return root[node]
        
            
        def union(x, y):
            
            rootx, rooty = find(x), find(y)
            
            if rootx == rooty:
                return
            
            if rank[rootx] < rank[rooty]:
                root[rooty] = rootx
                rank[rootx] += rank[rooty]
                
            else:
                root[rootx] = rooty
                rank[rooty] += rank[rootx]
                
                
                
        for i, j in edges:
            union(i, j)
            
        roots = set()
        for i in range(n):
            roots.add(find(i))
            
        roots = list(roots)
        
        
        ans = 0
        nodes_seen = 0
        for i in range(len(roots)):
            ans += rank[roots[i]] * (n - rank[roots[i]] - nodes_seen)
            nodes_seen += rank[roots[i]]
                
        return ans