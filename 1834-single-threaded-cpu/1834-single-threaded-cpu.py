class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort(key=lambda i: i[0])
        
        heap = []
        i = 0
        cur_time = tasks[0][0]
        ans = []
        
        
        while i < n:
            if not heap:
                new_time = tasks[i][0]
                while i < n and tasks[i][0] <= cur_time:
                    
                    task = [tasks[i][1], tasks[i][-1], tasks[i][0]]
                    heappush(heap, task)
                    i += 1
                
                
            if heap:
                time, idx, _ = heappop(heap)
                ans.append(idx)
                cur_time += time
                
                while i < n:
                    
                    if tasks[i][0] <= cur_time:
                        task = [tasks[i][1], tasks[i][-1], tasks[i][0]]
                        heappush(heap, task)
                        i += 1
                    else:
                        break
            else:
                cur_time = tasks[i][0]
        
        
        while heap:
            time, idx, _ = heappop(heap)
            ans.append(idx)
                    
        return ans
                    