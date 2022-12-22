class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = max(len(word1), len(word2))
        merged = ''
        ctr = 0
        while ctr < m:
            if ctr < len(word1) and ctr < len(word2):
                merged += word1[ctr]
                merged += word2[ctr]
            elif ctr >= len(word1):
                merged += word2[ctr]
            else:
                merged += word1[ctr]
            ctr += 1

        return merged

