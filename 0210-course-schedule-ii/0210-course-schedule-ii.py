class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre = [0] * numCourses
        graph = defaultdict(list)
        
        for i, j in prerequisites:
            pre[i] += 1
            graph[j].append(i)
            
            
        queue = deque()
        for i in range(numCourses):
            if pre[i] == 0:
                queue.append(i)
        
        
        order = []
        while queue:
            cur = queue.popleft()
            order.append(cur)
            
            for child in graph[cur]:
                pre[child] -= 1
                
                if pre[child] == 0:
                    queue.append(child)
                    
        if len(order) == numCourses:
            return order
        
        return []
            
            