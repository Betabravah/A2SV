class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = [0] * n
        
        if n == 1:
            return [0]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
            count[i] += 1
            count[j] += 1
            
            

            
        height = 0
        queue = deque([i for i in range(n) if count[i] == 1])


        while queue:
            
            length = len(queue)
            ans = []
            
            for _ in range(length):
                cur = queue.popleft()
                ans.append(cur)
                
                for child in graph[cur]:
                    count[child] -= 1

                    if count[child] == 1:
                        queue.append(child)

                

        return ans

        
                        
            
        