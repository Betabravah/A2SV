class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        
        for idx, char in enumerate(s):
            last_index[char] = idx
            
        got = set()
        stack = []
        
        for idx, char in enumerate(s):
            if char not in got:
                while stack and stack[-1] > char and last_index[stack[-1]] > idx:
                    got.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                got.add(char)
            
        return ''.join(stack)
            
