class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = 0
        _dict = {}
        stack = []
        for char in s:
            if char not in _dict.keys():
                _dict[char] = idx
                stack.append(1)
            else:
                first = _dict[char]
                curIdx = idx
                elem = 1
                while curIdx > first:
                    curIdx -= stack[-1]
                    elem += stack[-1]
                    stack.pop()
                stack.append(elem)
            idx += 1
        return stack
