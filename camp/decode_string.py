class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        decoded = []
        for i in s:
            if i == ']':
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(string * num)
            else:
                stack.append(i)
        if len(stack) == 1 and stack[0].isdigit():
            return ""
        return ''.join(stack)
