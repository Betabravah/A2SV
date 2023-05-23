class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root = [i for i in range(len(s))]
        rank = [1] * len(s)
        group = [set([i]) for i in range(len(s))]
        
        
        
        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
                
            return root[node]
        
        
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            
            if rootx == rooty:
                return
            
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1
            
            
            if rank[rootx] > rank[rooty]:
                root[rooty] = rootx
                rank[rootx] += 1
                group[rootx].update(group[rooty])
                
            else:
                root[rootx] = rooty
                rank[rooty] += 1
                group[rooty].update(group[rootx])
                
                
                
        for i, j in pairs:
            union(i, j)
            
        for i in range(len(s)):
            group[i] = sorted(group[i], key=lambda x: s[x] )
            group[i].append(0)
            
        
            
        ans = []
        for i in range(len(s)):
            parent = find(i)
            last = group[parent][-1]
            available = group[parent][last]
            ans.append(s[available])
            group[parent][-1] += 1
            
            
        return ''.join(ans)
            
                
                
            