class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * n
        
        for i, j in richer:
            graph[i].append(j)
            indegree[j] += 1
            
            
        queue = deque([i for i,x in enumerate(indegree) if x == 0])
        ans = ans = list(range(n))
        
        while queue:
            cur = queue.popleft()
            minn = ans[cur]
            
            for child in graph[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
                ans[child] = min(minn, ans[child], key=lambda x:quiet[x])
                
        return ans
                    
        
        
        