class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        n = len(s)
        
        for i in range(n):
            if stack:
                if s[stack[-1]] == '(' and s[i] == ')':
                    stack.pop()
                elif s[i] == '(' or s[i] == ')':
                    stack.append(i)
            else:
                if s[i] == '(' or s[i] == ')':
                    stack.append(i)
                    
          
        seen = set(stack)
        ans = []
        
        for i in range(n):
            if i not in seen:
                ans.append(s[i])
                
        return ''.join(ans)