class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []
        x = 1
        for i in s:
            if i == ')':
                num = 0
                isEmpty = True
                while stack[-1] != '(':
                    isEmpty = False
                    num += stack.pop()

                stack.pop()
                if stack and isEmpty:
                    stack.append(1)
                elif not stack and isEmpty:
                    score += 1
                elif stack:
                    stack.append(2 * num)
                else:
                    score += (2 * num)
            else:
                stack.append(i)

        return score
