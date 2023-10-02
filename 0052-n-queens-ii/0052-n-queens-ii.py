class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()
        negDiag = set()
        
        ans = 0
        
        def backtrack(q):
            nonlocal ans
            
            if q == n:
                ans += 1
                
            for col in range(n):
                if col in cols or (q - col) in posDiag or (q + col) in negDiag:
                    continue
                    
                cols.add(col)
                posDiag.add(q - col)
                negDiag.add(q + col)
                
                backtrack(q+1)
                
                cols.remove(col)
                posDiag.remove(q - col)
                negDiag.remove(q + col)
                
                
        backtrack(0)
        return ans