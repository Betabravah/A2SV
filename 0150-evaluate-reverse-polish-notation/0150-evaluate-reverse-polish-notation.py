class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(i, j, op):
            if op == '+':
                return i + j
            
            elif op == '-':
                return j - i
            
            elif op == '*':
                return i * j
            
            else:
                return int(j / i)
            
            
        stack = []
        
        for i in tokens:
            if i.isdigit() or i[1:].isdigit():                
                stack.append(int(i))
                
            else:
                
                val = evaluate(stack.pop(), stack.pop(), i)
                stack.append(val)
                
        return stack[0]