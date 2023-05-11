class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        
        
        count = [0] * n
        for i, j in edges:
            count[j] += 1
            graph[i].append(j)
        
        
        queue = deque()
        for i in range(n):
            if count[i] == 0:
                queue.append(i)
        
        
        output = [set() for i in range(n)]
        while queue:
            cur = queue.popleft()
            
            for child in graph[cur]:
                count[child] -= 1
                output[child] = output[child] | output[cur]
                output[child].add(cur)
                
                if count[child] == 0:
                    queue.append(child)
                    
                    
        answer = [sorted(list(output[i])) for i in range(n)]
        return answer
            
            
            
            
            