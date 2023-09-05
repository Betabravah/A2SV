class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [0 for i in range(n)]
        
        for node1, node2 in roads:
            graph[node1] += 1
            graph[node2] += 1
            
            
        
        graph.sort()
        
        ans = 0
        for i in range(1, n+1):
            ans += (graph[i-1] * i)
            
        return ans
        