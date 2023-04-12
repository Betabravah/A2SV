class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        
        answer = []
        def dfs(cur, path):
            # path.append(cur)
            
            if cur == target:
                answer.append(path.copy() + [cur])
                

            
            for i in graph[cur]:
                dfs(i, path + [cur])
                
        dfs(0, [])
        return answer