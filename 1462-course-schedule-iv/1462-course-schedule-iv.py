class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        count = [0] * numCourses
        graph = defaultdict(list)
        ancestor = defaultdict(set)
        
        for i, j in prerequisites:
            graph[i].append(j)
            count[j] += 1
            
            
        queue = deque()
        for i in range(numCourses):
            if count[i] == 0:
                queue.append(i)
                
                
        while queue:
            cur = queue.popleft()
            
            for child in graph[cur]:
                count[child] -= 1
                ancestor[child].add(cur)
                ancestor[child].update(ancestor[cur])
                
                if count[child] == 0:
                    queue.append(child)
                    
        
        ans = []        
        for i, j in queries:
            ans.append(i in ancestor[j])
            
        return ans