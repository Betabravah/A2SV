class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], times: List[int]) -> int:
        incoming = [0] * (n+1)
        graph = defaultdict(list)
        months = [i for i in times]
        
        
        for a, b in relations:
            graph[a].append(b)
            incoming[b] += 1
            
        
        queue = deque()
        for i in graph:
            if incoming[i] == 0:
                queue.append(i)
                
        
        ans = max(times)
        while queue:
            length = len(queue)
            
            for _ in range(length):
                cur = queue.popleft()
                
                ans = max(ans, months[cur-1])
                
                for child in graph[cur]:
                    months[child-1] = max(months[child-1], months[cur-1] + times[child-1])
                    
                    incoming[child] -= 1
                    
                    if incoming[child] == 0:
                        queue.append(child)
                        
        return ans