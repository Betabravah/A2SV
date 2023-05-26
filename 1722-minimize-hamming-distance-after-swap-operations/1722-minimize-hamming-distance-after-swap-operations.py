class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        
        root = [i for i in range(n)]
        rank = [1] * n
        group = [{source[i]:1} for i in range(n)]
        
        
        def merge(a, b):
            result = {}
            for key in set(a.keys()) | set(b.keys()):
                result[key] = a.get(key, 0) + b.get(key, 0)

            return result

        
        
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
                group[rootx] = merge(group[rootx], group[rooty])
                
            else:
                root[rootx] = rooty
                rank[rooty] += 1
                group[rooty] = merge(group[rootx], group[rooty])
                
                
                
                
        for i, j in allowedSwaps:
            union(i, j)

        
        ans = 0
        for i in range(n):
            parent = find(i)

            exists = group[parent].get(target[i], 0)
            
            if exists > 0 :
                group[parent][target[i]] -= 1
                
            else:
                ans += 1
                
        return ans
                
            
            