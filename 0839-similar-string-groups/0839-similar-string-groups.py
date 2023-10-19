class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def equivalent(a, b):
            
            if len(a) != len(b):
                return False
            
            prev = None
            got2diff = False
            
            for i in range(len(a)):
                if a[i] != b[i]:
                    if got2diff:
                        return False
                    
                    if not prev:
                        prev = a[i]
                        
                    else:
                        if b[i] != prev:
                            return False
                        got2diff = True
                        
            return True
        
        
        
        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
                
            return root[node]
        
        
        def union(x, y):
            rootx, rooty = find(x), find(y)  
            rankx, ranky = rank[rootx], rank[rooty]
            
            if rankx == ranky:
                rankx += 1
                
            if rankx > ranky:
                root[rooty] = rootx
                rank[rootx] += 1
                
            else:
                root[rootx] = rooty
                rank[rooty] += 1
        
        root = [i for i in range(len(strs))]
        rank = [1] * len(strs)
        
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if equivalent(strs[i], strs[j]):
                    union(i, j)
                    
        ans = 0
        for i in range(len(strs)):
            if root[i] == i:
                ans += 1
                
        return ans
                    
                    