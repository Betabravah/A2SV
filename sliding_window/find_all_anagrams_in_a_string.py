class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        pCount, sCount = {}, {}
        if len(p) > len(s):
            return []
        for i in range(len(p)): # build window with len(p)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
        indices=[0] if pCount == sCount else [] # check if window is anagram

        start = 0
        for end in range(len(p), len(s)): # slide window
            sCount[s[end]] = 1 + sCount.get(s[end], 0)
            sCount[s[start]] -= 1
            
            if sCount[s[start]] == 0:
                sCount.pop(s[start])
            start += 1
            if sCount == pCount:
                indices.append(start)
        
        return indices