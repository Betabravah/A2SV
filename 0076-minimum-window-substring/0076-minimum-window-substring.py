class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(str1, str2):
            return all(str1[i] >= str2[i] for i in str2)
        
        
        tcount = Counter(t)
        start = end = -1
        left = 0
        minLen = len(s)+1
        scount = defaultdict(int)
        
        
        for right in range(len(s)):
            scount[s[right]] += 1
            
            while contains(scount, tcount):
                if right - left + 1< minLen:
                    start, end = left, right
                    minLen = right - left + 1
                    
                    
                scount[s[left]] -= 1
                left += 1
                
                
        return '' if minLen == len(s)+1 else s[start:end+1]
                
        