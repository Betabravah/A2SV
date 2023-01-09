class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxLen = 0
        words = s.split()
        for word in words:
            maxLen = max(maxLen, len(word))

        verticals = []
        for idx in range(maxLen):
            vertical = []
            for word in words:
                if len(word) > idx:
                    vertical.append(word[idx])
                else:
                    vertical.append(' ')
            vertical = ''.join(vertical)
            vertical = vertical.rstrip()
            verticals.append(vertical)

        return verticals
