class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings.sort(key=lambda x: x[2])
        
        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
                
            return root[node]
        
        
        def union(x, y):
            rootx, rooty = find(x), find(y)  
            rankx, ranky = rank[rootx], rank[rooty]
            
            if rankx == ranky:
                rankx += 1
                
            if rankx > ranky:
                root[rooty] = rootx
                rank[rootx] += 1
                
            else:
                root[rootx] = rooty
                rank[rooty] += 1
               
            
        def ungroup(i, j):
            secret_root = find(0)
            
            while i <= j:
                x, y, _ = meetings[i]
                cur_root = find(x)
                
                if cur_root != secret_root:
                    root[x] = x
                    root[y] = y
                
                i += 1
                

        
        
        root = [i for i in range(n)]
        rank = [1] * n
        
        union(0, firstPerson)
        
        left = 0
        
        while left < len(meetings):
            right = left
            
            while right < len(meetings) and meetings[left][2] == meetings[right][2]:
                x, y, _ = meetings[right]
                
                union(x, y)
                right += 1
                
            ungroup(left, right-1)
            left = right
            
        
        
        ans = []
        secret_root = find(0)
        
        for i in range(n):
            cur_root = find(i)
            
            if cur_root == secret_root:
                ans.append(i)
                
        return ans
            
            
            