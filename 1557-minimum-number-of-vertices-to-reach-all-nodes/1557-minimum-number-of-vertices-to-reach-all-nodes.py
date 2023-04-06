class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        
        for frm, to in edges:
            indegree[to] += 1
        
        ans = []
        for i, count in enumerate(indegree):
            if count == 0:
                ans.append(i)
                
        return ans
                
            