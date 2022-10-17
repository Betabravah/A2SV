class Solution:
    def decodeString(self, s: str) -> str:
        stack = ""

        for i in s:    
            if i == "]":
                curr = i
                currText = ""
                while curr != "[":
                    currText += stack[-1]
                    stack = stack[:len(stack)-1]
                    curr = stack[-1]
                stack = stack[:len(stack)-1]
                curr = stack[-1]

                num = ""
                try:
                    while curr.isnumeric() and len(stack) >= 1:
                        num += stack[-1]
                        stack = stack[:len(stack)-1]
                        curr = stack[-1]
                except:
                    pass
                num = num[::-1]
                currText = currText * int(num)
                stack += currText[::-1]
            else:
                stack += i

        return stack
