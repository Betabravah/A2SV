class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        for idx, space in enumerate(spaces):
            if idx == 0:
                words.append(s[:space])
            else:
                startIdx = spaces[idx-1]
                words.append(s[startIdx:space])
        words.append(s[space:])
        
        return ' '.join(words)
