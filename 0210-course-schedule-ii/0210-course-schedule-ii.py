class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre = [0] * numCourses
        graph = defaultdict(list)
        
        for i, j in prerequisites:
            pre[j] += 1
            graph[j].append(i)
            
            
        stack = []
        for i in range(numCourses):
            if pre[i] == 0:
                stack.append(i)
        
        
        order = []
        color = [0] * numCourses # 0 - white, 1 - grey, 2 - black
        is_cyclic = False
        
        def dfs(cur):
            nonlocal is_cyclic
            nonlocal order
            
            
            color[cur] = 1
            
            for child in graph[cur]:
                
                if color[child] == 1:
                    is_cyclic = True
                    return 
                
                if color[child] == 0:
                    dfs(child)
            
            
            color[cur] = 2
            order.append(cur)
            
            
        
        for i in range(numCourses):
            if is_cyclic:
                return []
            if color[i] != 2:
                dfs(i)  
            
        return order[::-1]
        
            
            