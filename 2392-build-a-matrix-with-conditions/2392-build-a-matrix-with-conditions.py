class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def helper(conditions):
            graph = [[] for _ in range(k)]
            count = [0 for _ in range(k)]

            for a, b in conditions:
                graph[a-1].append(b-1)
                count[b-1] += 1


            queue = deque()
            for i in range(k):
                if count[i] == 0:
                    queue.append(i)

            ans = []
            while queue:
                
                cur = queue.popleft()
                ans.append(cur)

                for child in graph[cur]:
                    count[child] -= 1

                    if count[child] == 0:
                        queue.append(child)
            
            return ans if len(ans) == k else None


        arr1, arr2 = helper(rowConditions), helper(colConditions)
        
        if not arr1 or not arr2:
            return []
        
        ans = [[0] * k for _ in range(k)]
        
        for i in range(k):
            ans[arr1.index(i)][arr2.index(i)] = i + 1
            
            
        return ans



