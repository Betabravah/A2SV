class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        idx = 0
        
        while idx < len(s):
            i = s[idx]
            
            if i.isdigit():
                
                while idx+1 < len(s):
                    if s[idx+1].isdigit():
                        i += s[idx+1]
                    else:
                        break
                    idx += 1
                    
                if stack and stack[-1] == '*':
                    stack.pop()
                    
                    prev_num = int(stack.pop())
                    stack.append(str(int(i) * prev_num))
                    
                
                elif stack and stack[-1] == '/':
                    stack.pop()
                    
                    prev_num = int(stack.pop())
                    print(prev_num, prev_num // int(i))
                    stack.append(str(prev_num // int(i)))
                    
                elif stack and stack[-1].isdigit():
                    stack[-1] += i
                    
                else:
                    stack.append(i)
                    
            elif i in ['+', '-', '*', '/']:
                stack.append(i)
                
            idx += 1
                
        print(stack)
        i = ans = 0
        neg = False
        
        while i < len(stack):
            if stack[i] == '-':
                neg = True
                
            elif stack[i] == '+':
                neg = False
                
            elif stack[i].isdigit():
                if neg:
                    ans -= int(stack[i])
                else:
                    ans += int(stack[i])
                    
            i += 1
            
        return ans
                
            
                    
            
            