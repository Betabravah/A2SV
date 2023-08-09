class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        cookie = ctr = 0
        for i in range(len(g)):
            if cookie >= len(s):
                break
                
            elif s[cookie] >= g[i]:
                ctr += 1
                cookie += 1
                
        return cookie
