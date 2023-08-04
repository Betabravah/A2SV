from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for u, v in edges:
            graph[u-1].append(v-1)
            incoming[v-1] += 1
        
        
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append((i, 1))


        ans = [-1] * n 
        while queue:
            cur, time = queue.popleft()
            ans[cur] = time
            
            for child in graph[cur]:
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    queue.append((child, time+1))


        return ans
            



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends