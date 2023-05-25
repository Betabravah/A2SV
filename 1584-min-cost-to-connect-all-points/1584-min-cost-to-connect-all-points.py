class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        if len(points) <= 1:
            return 0
        
        
        points = [tuple(i) for i in points]
        n = len(points)
        root = {i:i for i in points}
        rank = {i:1 for i in points}
        
        
        
        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
                
            return root[node]
        
        
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            
            if rootx == rooty:
                return False
            
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1
            
            
            if rank[rootx] > rank[rooty]:
                root[rooty] = rootx
                rank[rootx] += 1

                
            else:
                root[rootx] = rooty
                rank[rooty] += 1
            
            return True
                
                
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        
        def create_heap(points):
            heap = []
            
            for i in range(n):
                for j in range(i+1, n):
                    heappush(heap, [distance(points[i], points[j]), points[i], points[j]])
                    
            return heap
                    
        
        
        
        
        total = ctr = 0
        heap = create_heap(points)
        while heap:
            
            if ctr == n - 1:
                break
                    
            distance, p1, p2 = heappop(heap)
            
            if union(p1, p2):
                total += distance
                ctr += 1

            
            
        return total
            
        
                    
                    
                
            