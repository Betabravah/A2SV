class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        def dfs(node):
            nonlocal ans
            
            visited[node] = True
            sums = values[node]
            
            temp = 0
            for neigh in graph[node]:
                if visited[neigh]: continue
                    
                temp = dfs(neigh)
                
                if temp % k == 0:
                    ans += 1
                else:
                    sums += temp
                    
            return sums
        
        ans = 1
        visited = [False] * n
        dfs(0)
        return ans