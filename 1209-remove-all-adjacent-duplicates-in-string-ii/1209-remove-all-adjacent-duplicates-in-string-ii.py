class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for idx, i in enumerate(s):
            if stack:
                if stack[-1][0] == i:
                    prev = stack[-1][1]
                    stack.append([i, prev + 1])
                else:
                    stack.append([i, 1])
                    
            else:
                stack.append([i, 1])
                
                    
            if len(stack) >= k and stack[-1][1] == k:
                stack = stack[:-k]
                
                
                
        ans = []
        for i, j in stack:
            ans.append(i)
            
        return ''.join(ans)
            
            
                