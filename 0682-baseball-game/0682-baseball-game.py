class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for i in operations:
            if i  == 'C':
                stack.pop()
            elif i == 'D':
                new = stack[-1] * 2
                stack.append(new)
            elif i == '+':
                new = stack[-1] + stack[-2]
                stack.append(new)
            else:
                stack.append(int(i))
                
        return sum(stack)
                
            