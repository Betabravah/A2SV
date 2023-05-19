class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = defaultdict(int)
        
        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
            
            count[i] += 1
            count[j] += 1
            
        got = False 
        queue = deque()
        for i, j in count.items():
            if j == 1:
                if not got:
                    queue.append(i)
                    got = True
                    
                else:
                    last = i

                
        ans = []
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for child in graph[cur]:
                count[child] -= 1
                
                if count[child] == 1:
                    queue.append(child)
                    
        ans.append(last)     
        return ans
        