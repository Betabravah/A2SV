class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [i for i in range(1, n+1)]        
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        
        
        suffix  = [i for i in range(1, n+1)]
        for i in range(n-2, -1, -1):
            suffix[i] += suffix[i+1]
        
        
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i+1
            
        return -1

            
        