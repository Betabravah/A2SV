class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = []
        reverse = ""
        
        for i in s:
            if i == ")":
                while stack[-1] != "(":
                    queue.append(stack.pop())
                stack.pop()

                while queue:
                    stack.append(queue[0])
                    queue.__delitem__(0)

            else:
                stack.append(i)
        
        for i in stack:
            reverse += i
            
        return reverse
            
                