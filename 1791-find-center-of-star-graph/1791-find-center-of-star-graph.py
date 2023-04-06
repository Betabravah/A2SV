class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        
        for edge in edges:
            if freq[edge[0]] > 0:
                return edge[0]
            if freq[edge[1]] > 0:
                return edge[1]
            
            freq[edge[0]] += 1
            freq[edge[1]] += 1
            
            