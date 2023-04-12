class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjacency = defaultdict(list)
        
        for frm, to in roads:
            adjacency[frm].append(to)
            adjacency[to].append(frm)

        max_rank = 0
        for i in range(n):
            rank = len(adjacency[i])
            
            for j in range(n):
                if j == i:
                    continue
                if j in adjacency[i]:
                    max_rank = max(max_rank, rank + len(adjacency[j]) - 1)
                else:
                    max_rank = max(max_rank, rank + len(adjacency[j])) 
                
                
        return max_rank
                
                
            
            