class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(opened, closed, cur):
            nonlocal ans
            
            if opened > n or closed > n:
                return
            
            if opened == closed == n:
                ans.append(cur)
                return
            
            if opened == closed:
                backtrack(opened+1, closed, cur + '(')
            
            if closed < opened:
                backtrack(opened + 1, closed, cur + '(')
                backtrack(opened, closed + 1, cur + ')')
                
        ans = []
        backtrack(0, 0, '')
        return ans