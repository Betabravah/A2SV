class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        heap = []
        for i in range(n):
            for j in range(n):
                heappush(heap, matrix[i][j])
                
                
        for i in range(k):
            x = heappop(heap)
        return x