class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n, m = len(graph), len(graph[0])
        safe = []
        
        children = defaultdict(list)
        count = [0] * n
        queue = deque()
        
        for i in range(n):
            if graph[i] == []:
                queue.append(i)
                safe.append(i)
                continue
                
            for j in graph[i]:
                children[j].append(i)
                count[i] += 1
                
        # print(children, count)
        
        while queue:
            cur = queue.popleft()
            
            for child in children[cur]:
                count[child] -= 1
                
                if count[child] == 0:
                    queue.append(child)
                    safe.append(child)
                    
        safe.sort()    
        return safe
            
            
            
            
                
        # for i in range(len(graph)):
            
            