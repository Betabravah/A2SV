class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = defaultdict(int)
        trusters = set()
        
        for i, j in trust:
            
            trusters.add(i)
                
            count[j] += 1

            
        for i in range(1, n+1):
            if count[i] == n-1 and i not in trusters:
                return i
            
        return -1