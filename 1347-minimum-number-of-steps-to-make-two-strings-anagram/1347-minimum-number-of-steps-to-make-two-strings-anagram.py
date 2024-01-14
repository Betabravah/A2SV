class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq1 = Counter(s)
        freq2 = Counter(t)
        
        ans = 0
        for i in freq1:
            if freq1[i] > freq2[i]:
                ans += (freq1[i] - freq2[i])
            
            
        return ans 